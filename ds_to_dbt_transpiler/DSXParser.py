# Generated from ds_to_dbt_transpiler/DSX.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,62,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,24,8,1,10,1,12,1,27,9,
        1,1,1,1,1,1,2,1,2,1,2,1,2,5,2,35,8,2,10,2,12,2,38,9,2,1,2,1,2,1,
        3,1,3,1,3,5,3,45,8,3,10,3,12,3,48,9,3,1,3,1,3,1,4,1,4,1,4,1,5,1,
        5,1,5,1,6,1,6,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,0,58,0,16,1,
        0,0,0,2,19,1,0,0,0,4,30,1,0,0,0,6,41,1,0,0,0,8,51,1,0,0,0,10,54,
        1,0,0,0,12,57,1,0,0,0,14,59,1,0,0,0,16,17,3,2,1,0,17,18,5,0,0,1,
        18,1,1,0,0,0,19,20,5,1,0,0,20,25,3,8,4,0,21,24,3,10,5,0,22,24,3,
        4,2,0,23,21,1,0,0,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,
        26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,29,5,2,0,0,29,3,1,0,0,
        0,30,31,5,3,0,0,31,36,3,8,4,0,32,35,3,10,5,0,33,35,3,6,3,0,34,32,
        1,0,0,0,34,33,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,
        37,39,1,0,0,0,38,36,1,0,0,0,39,40,5,4,0,0,40,5,1,0,0,0,41,42,5,5,
        0,0,42,46,3,8,4,0,43,45,3,10,5,0,44,43,1,0,0,0,45,48,1,0,0,0,46,
        44,1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,46,1,0,0,0,49,50,5,6,0,
        0,50,7,1,0,0,0,51,52,5,7,0,0,52,53,3,14,7,0,53,9,1,0,0,0,54,55,3,
        12,6,0,55,56,3,14,7,0,56,11,1,0,0,0,57,58,5,8,0,0,58,13,1,0,0,0,
        59,60,5,9,0,0,60,15,1,0,0,0,5,23,25,34,36,46
    ]

class DSXParser ( Parser ):

    grammarFileName = "DSX.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'BEGIN DSJOB'", "'END DSJOB'", "'BEGIN DSSTAGE'",
                     "'END DSSTAGE'", "'BEGIN DSRECORD'", "'END DSRECORD'",
                     "'Identifier'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "NAME", "STRING", "WS" ]

    RULE_dsx = 0
    RULE_dsjob = 1
    RULE_dsstage = 2
    RULE_dsrecord = 3
    RULE_identifier = 4
    RULE_property = 5
    RULE_propname = 6
    RULE_propvalue = 7

    ruleNames =  [ "dsx", "dsjob", "dsstage", "dsrecord", "identifier",
                   "property", "propname", "propvalue" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    NAME=8
    STRING=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DsxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dsjob(self):
            return self.getTypedRuleContext(DSXParser.DsjobContext,0)


        def EOF(self):
            return self.getToken(DSXParser.EOF, 0)

        def getRuleIndex(self):
            return DSXParser.RULE_dsx

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDsx" ):
                listener.enterDsx(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDsx" ):
                listener.exitDsx(self)




    def dsx(self):

        localctx = DSXParser.DsxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_dsx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.dsjob()
            self.state = 17
            self.match(DSXParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DsjobContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(DSXParser.IdentifierContext,0)


        def property_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSXParser.PropertyContext)
            else:
                return self.getTypedRuleContext(DSXParser.PropertyContext,i)


        def dsstage(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSXParser.DsstageContext)
            else:
                return self.getTypedRuleContext(DSXParser.DsstageContext,i)


        def getRuleIndex(self):
            return DSXParser.RULE_dsjob

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDsjob" ):
                listener.enterDsjob(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDsjob" ):
                listener.exitDsjob(self)




    def dsjob(self):

        localctx = DSXParser.DsjobContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_dsjob)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(DSXParser.T__0)
            self.state = 20
            self.identifier()
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==8:
                self.state = 23
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8]:
                    self.state = 21
                    self.property_()
                    pass
                elif token in [3]:
                    self.state = 22
                    self.dsstage()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(DSXParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DsstageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(DSXParser.IdentifierContext,0)


        def property_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSXParser.PropertyContext)
            else:
                return self.getTypedRuleContext(DSXParser.PropertyContext,i)


        def dsrecord(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSXParser.DsrecordContext)
            else:
                return self.getTypedRuleContext(DSXParser.DsrecordContext,i)


        def getRuleIndex(self):
            return DSXParser.RULE_dsstage

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDsstage" ):
                listener.enterDsstage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDsstage" ):
                listener.exitDsstage(self)




    def dsstage(self):

        localctx = DSXParser.DsstageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dsstage)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(DSXParser.T__2)
            self.state = 31
            self.identifier()
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==8:
                self.state = 34
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8]:
                    self.state = 32
                    self.property_()
                    pass
                elif token in [5]:
                    self.state = 33
                    self.dsrecord()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(DSXParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DsrecordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(DSXParser.IdentifierContext,0)


        def property_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSXParser.PropertyContext)
            else:
                return self.getTypedRuleContext(DSXParser.PropertyContext,i)


        def getRuleIndex(self):
            return DSXParser.RULE_dsrecord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDsrecord" ):
                listener.enterDsrecord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDsrecord" ):
                listener.exitDsrecord(self)




    def dsrecord(self):

        localctx = DSXParser.DsrecordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_dsrecord)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(DSXParser.T__4)
            self.state = 42
            self.identifier()
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 43
                self.property_()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self.match(DSXParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def propvalue(self):
            return self.getTypedRuleContext(DSXParser.PropvalueContext,0)


        def getRuleIndex(self):
            return DSXParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)




    def identifier(self):

        localctx = DSXParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(DSXParser.T__6)
            self.state = 52
            self.propvalue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def propname(self):
            return self.getTypedRuleContext(DSXParser.PropnameContext,0)


        def propvalue(self):
            return self.getTypedRuleContext(DSXParser.PropvalueContext,0)


        def getRuleIndex(self):
            return DSXParser.RULE_property

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProperty" ):
                listener.enterProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProperty" ):
                listener.exitProperty(self)




    def property_(self):

        localctx = DSXParser.PropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_property)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.propname()
            self.state = 55
            self.propvalue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(DSXParser.NAME, 0)

        def getRuleIndex(self):
            return DSXParser.RULE_propname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropname" ):
                listener.enterPropname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropname" ):
                listener.exitPropname(self)




    def propname(self):

        localctx = DSXParser.PropnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_propname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(DSXParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(DSXParser.STRING, 0)

        def getRuleIndex(self):
            return DSXParser.RULE_propvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropvalue" ):
                listener.enterPropvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropvalue" ):
                listener.exitPropvalue(self)




    def propvalue(self):

        localctx = DSXParser.PropvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_propvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(DSXParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
