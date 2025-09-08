import xml.etree.ElementTree as ET

# Re-using the same data structures as the DSX parser for consistency
class JobInfo:
    def __init__(self):
        self.name = None
        self.stages = []

class StageInfo:
    def __init__(self):
        self.name = None
        self.properties = {}
        self.records = []

class RecordInfo:
    def __init__(self):
        self.name = None
        self.properties = {}

class XMLParser:
    def __init__(self, filepath):
        self.tree = ET.parse(filepath)
        self.root = self.tree.getroot()

    def parse(self):
        job_info = JobInfo()
        job_element = self.root.find('DSJob')
        if job_element is not None:
            job_info.name = job_element.get('Name')
            for stage_element in job_element.findall('DSStage'):
                stage_info = StageInfo()
                stage_info.name = stage_element.get('Name')
                stage_info.properties['StageType'] = stage_element.get('Type')

                for record_element in stage_element.findall('DSRecord'):
                    record_info = RecordInfo()
                    record_info.name = record_element.get('Name')
                    for prop_element in record_element.findall('Property'):
                        prop_name = prop_element.get('Name')
                        prop_value = prop_element.text
                        record_info.properties[prop_name] = prop_value
                    stage_info.records.append(record_info)
                job_info.stages.append(stage_info)
        return job_info

# For testing
if __name__ == '__main__':
    parser = XMLParser('ds_to_dbt_transpiler/sample.xml')
    job_info = parser.parse()

    if job_info:
        print(f"Successfully parsed job: {job_info.name}")
        for stage in job_info.stages:
            print(f"  Stage: {stage.name}, Type: {stage.properties.get('StageType')}")
            for record in stage.records:
                print(f"    Record: {record.name}")
                for prop, value in record.properties.items():
                    print(f"      Property: {prop} = {value}")
    else:
        print("Failed to parse the XML content.")
