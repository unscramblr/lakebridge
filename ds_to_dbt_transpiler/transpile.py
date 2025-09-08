import os
import argparse
from antlr4 import *
from DSXLexer import DSXLexer
from DSXParser import DSXParser
from DSXListener import DSXListener
from xml_parser import XMLParser, JobInfo as XMLJobInfo

# Using the JobInfo from the XML parser as the canonical one
class JobInfo(XMLJobInfo):
    pass

class DSXJobInfoListener(DSXListener):
    def __init__(self):
        self.job_info = JobInfo()
        self.current_stage = None
        self.current_record = None

    def enterDsjob(self, ctx:DSXParser.DsjobContext):
        self.job_info.name = ctx.identifier().propvalue().getText().strip('"')

    def enterDsstage(self, ctx:DSXParser.DsstageContext):
        from xml_parser import StageInfo # avoid circular import at top level
        self.current_stage = StageInfo()
        self.current_stage.name = ctx.identifier().propvalue().getText().strip('"')
        self.job_info.stages.append(self.current_stage)

    def exitDsstage(self, ctx:DSXParser.DsstageContext):
        self.current_stage = None

    def enterDsrecord(self, ctx:DSXParser.DsrecordContext):
        from xml_parser import RecordInfo
        self.current_record = RecordInfo()
        self.current_record.name = ctx.identifier().propvalue().getText().strip('"')
        if self.current_stage:
            self.current_stage.records.append(self.current_record)

    def exitDsrecord(self, ctx:DSXParser.DsrecordContext):
        self.current_record = None

    def enterProperty(self, ctx:DSXParser.PropertyContext):
        prop_name = ctx.propname().getText()
        prop_value = ctx.propvalue().getText().strip('"')
        if self.current_record:
            self.current_record.properties[prop_name] = prop_value
        elif self.current_stage:
            self.current_stage.properties[prop_name] = prop_value


def find_source_and_target_tables(job_info):
    source_table = None
    target_table = None
    for stage in job_info.stages:
        # Only look for real source/target tables in non-transformer stages
        if stage.properties.get('StageType') != 'Transformer':
            for record in stage.records:
                if 'Source' in record.properties:
                    source_table = record.properties['Source']
                if 'Target' in record.properties:
                    target_table = record.properties['Target']
    return source_table, target_table

def find_transform_stage(job_info):
    for stage in job_info.stages:
        if stage.properties.get('StageType') == 'Transformer':
            return stage
    return None


def create_dbt_project(job_info, output_dir="dbt_project"):
    source_table, target_table = find_source_and_target_tables(job_info)
    if not source_table or not target_table:
        raise Exception("Could not determine source and target tables")

    transform_stage = find_transform_stage(job_info)
    if not transform_stage:
        raise Exception("Could not find a Transformer stage")

    project_output_dir = os.path.join(os.path.dirname(__file__), output_dir)
    models_dir = os.path.join(project_output_dir, "models", "staging")
    os.makedirs(models_dir, exist_ok=True)
    dbt_project_yml_content = f"""
name: '{target_table}_project'
version: '1.0.0'
config-version: 2
profile: 'default'
model-paths: ["models"]
"""
    with open(os.path.join(project_output_dir, "dbt_project.yml"), "w") as f:
        f.write(dbt_project_yml_content)
    staging_model_sql = f"SELECT * FROM {{{{ source('src', '{source_table}') }}}}\n"
    with open(os.path.join(models_dir, f"stg_{source_table}.sql"), "w") as f:
        f.write(staging_model_sql)
    staging_source_yml = f"""
version: 2
sources:
  - name: src
    tables:
      - name: {source_table}
"""
    with open(os.path.join(models_dir, "sources.yml"), "w") as f:
        f.write(staging_source_yml)
    transform_logic = transform_stage.records[0].properties.get('Transform', '')
    cols = []
    for part in transform_logic.split(','):
        if '=' in part:
            target_col, source_expr = part.split('=', 1)
            source_col = source_expr.split('.')[-1]
            cols.append(f"    {source_col} AS {target_col}")
    final_model_sql = f"""
SELECT
{",\\n".join(cols)}
FROM {{{{ ref('stg_{source_table}') }}}}
"""
    final_model_path = os.path.join(project_output_dir, "models", f"{target_table}.sql")
    with open(final_model_path, "w") as f:
        f.write(final_model_sql)

def main():
    arg_parser = argparse.ArgumentParser(description='Transpile a DataStage file to a dbt project.')
    arg_parser.add_argument('input_file', type=str, help='The path to the input .dsx or .xml file.')
    args = arg_parser.parse_args()

    print(f"Starting transpiler for {args.input_file}...")

    job_info = None
    if args.input_file.endswith('.xml'):
        parser = XMLParser(args.input_file)
        job_info = parser.parse()
    elif args.input_file.endswith('.dsx'):
        input_stream = FileStream(args.input_file)
        lexer = DSXLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = DSXParser(stream)
        tree = parser.dsx()
        listener = DSXJobInfoListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        job_info = listener.job_info
    else:
        print("Unsupported file type. Please provide a .dsx or .xml file.")
        return

    if job_info and job_info.name:
        print(f"Successfully parsed job: {job_info.name}")
        create_dbt_project(job_info, output_dir="dbt_project")
        print("dbt project created successfully.")
    else:
        print("Failed to parse the input file.")

if __name__ == "__main__":
    main()
