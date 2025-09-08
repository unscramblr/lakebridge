# Generated from ds_to_dbt_transpiler/DSX.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DSXParser import DSXParser
else:
    from DSXParser import DSXParser

# This class defines a complete listener for a parse tree produced by DSXParser.
class DSXListener(ParseTreeListener):

    # Enter a parse tree produced by DSXParser#dsx.
    def enterDsx(self, ctx:DSXParser.DsxContext):
        pass

    # Exit a parse tree produced by DSXParser#dsx.
    def exitDsx(self, ctx:DSXParser.DsxContext):
        pass


    # Enter a parse tree produced by DSXParser#dsjob.
    def enterDsjob(self, ctx:DSXParser.DsjobContext):
        pass

    # Exit a parse tree produced by DSXParser#dsjob.
    def exitDsjob(self, ctx:DSXParser.DsjobContext):
        pass


    # Enter a parse tree produced by DSXParser#dsstage.
    def enterDsstage(self, ctx:DSXParser.DsstageContext):
        pass

    # Exit a parse tree produced by DSXParser#dsstage.
    def exitDsstage(self, ctx:DSXParser.DsstageContext):
        pass


    # Enter a parse tree produced by DSXParser#dsrecord.
    def enterDsrecord(self, ctx:DSXParser.DsrecordContext):
        pass

    # Exit a parse tree produced by DSXParser#dsrecord.
    def exitDsrecord(self, ctx:DSXParser.DsrecordContext):
        pass


    # Enter a parse tree produced by DSXParser#identifier.
    def enterIdentifier(self, ctx:DSXParser.IdentifierContext):
        pass

    # Exit a parse tree produced by DSXParser#identifier.
    def exitIdentifier(self, ctx:DSXParser.IdentifierContext):
        pass


    # Enter a parse tree produced by DSXParser#property.
    def enterProperty(self, ctx:DSXParser.PropertyContext):
        pass

    # Exit a parse tree produced by DSXParser#property.
    def exitProperty(self, ctx:DSXParser.PropertyContext):
        pass


    # Enter a parse tree produced by DSXParser#propname.
    def enterPropname(self, ctx:DSXParser.PropnameContext):
        pass

    # Exit a parse tree produced by DSXParser#propname.
    def exitPropname(self, ctx:DSXParser.PropnameContext):
        pass


    # Enter a parse tree produced by DSXParser#propvalue.
    def enterPropvalue(self, ctx:DSXParser.PropvalueContext):
        pass

    # Exit a parse tree produced by DSXParser#propvalue.
    def exitPropvalue(self, ctx:DSXParser.PropvalueContext):
        pass



del DSXParser