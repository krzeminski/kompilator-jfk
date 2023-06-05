# Generated from Dallas.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .DallasParser import DallasParser
else:
    from DallasParser import DallasParser

# This class defines a complete listener for a parse tree produced by DallasParser.
class DallasListener(ParseTreeListener):

    # Enter a parse tree produced by DallasParser#prog.
    def enterProg(self, ctx:DallasParser.ProgContext):
        pass

    # Exit a parse tree produced by DallasParser#prog.
    def exitProg(self, ctx:DallasParser.ProgContext):
        pass


    # Enter a parse tree produced by DallasParser#statement.
    def enterStatement(self, ctx:DallasParser.StatementContext):
        pass

    # Exit a parse tree produced by DallasParser#statement.
    def exitStatement(self, ctx:DallasParser.StatementContext):
        pass


    # Enter a parse tree produced by DallasParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:DallasParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by DallasParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:DallasParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by DallasParser#assignment.
    def enterAssignment(self, ctx:DallasParser.AssignmentContext):
        pass

    # Exit a parse tree produced by DallasParser#assignment.
    def exitAssignment(self, ctx:DallasParser.AssignmentContext):
        pass


    # Enter a parse tree produced by DallasParser#printCall.
    def enterPrintCall(self, ctx:DallasParser.PrintCallContext):
        pass

    # Exit a parse tree produced by DallasParser#printCall.
    def exitPrintCall(self, ctx:DallasParser.PrintCallContext):
        pass


    # Enter a parse tree produced by DallasParser#readCall.
    def enterReadCall(self, ctx:DallasParser.ReadCallContext):
        pass

    # Exit a parse tree produced by DallasParser#readCall.
    def exitReadCall(self, ctx:DallasParser.ReadCallContext):
        pass


    # Enter a parse tree produced by DallasParser#functionCall.
    def enterFunctionCall(self, ctx:DallasParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by DallasParser#functionCall.
    def exitFunctionCall(self, ctx:DallasParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by DallasParser#functionCallOnObject.
    def enterFunctionCallOnObject(self, ctx:DallasParser.FunctionCallOnObjectContext):
        pass

    # Exit a parse tree produced by DallasParser#functionCallOnObject.
    def exitFunctionCallOnObject(self, ctx:DallasParser.FunctionCallOnObjectContext):
        pass


    # Enter a parse tree produced by DallasParser#functionCallOnString.
    def enterFunctionCallOnString(self, ctx:DallasParser.FunctionCallOnStringContext):
        pass

    # Exit a parse tree produced by DallasParser#functionCallOnString.
    def exitFunctionCallOnString(self, ctx:DallasParser.FunctionCallOnStringContext):
        pass


    # Enter a parse tree produced by DallasParser#array.
    def enterArray(self, ctx:DallasParser.ArrayContext):
        pass

    # Exit a parse tree produced by DallasParser#array.
    def exitArray(self, ctx:DallasParser.ArrayContext):
        pass


    # Enter a parse tree produced by DallasParser#toInt.
    def enterToInt(self, ctx:DallasParser.ToIntContext):
        pass

    # Exit a parse tree produced by DallasParser#toInt.
    def exitToInt(self, ctx:DallasParser.ToIntContext):
        pass


    # Enter a parse tree produced by DallasParser#toFloat.
    def enterToFloat(self, ctx:DallasParser.ToFloatContext):
        pass

    # Exit a parse tree produced by DallasParser#toFloat.
    def exitToFloat(self, ctx:DallasParser.ToFloatContext):
        pass


    # Enter a parse tree produced by DallasParser#expression.
    def enterExpression(self, ctx:DallasParser.ExpressionContext):
        pass

    # Exit a parse tree produced by DallasParser#expression.
    def exitExpression(self, ctx:DallasParser.ExpressionContext):
        pass


    # Enter a parse tree produced by DallasParser#or.
    def enterOr(self, ctx:DallasParser.OrContext):
        pass

    # Exit a parse tree produced by DallasParser#or.
    def exitOr(self, ctx:DallasParser.OrContext):
        pass


    # Enter a parse tree produced by DallasParser#xor.
    def enterXor(self, ctx:DallasParser.XorContext):
        pass

    # Exit a parse tree produced by DallasParser#xor.
    def exitXor(self, ctx:DallasParser.XorContext):
        pass


    # Enter a parse tree produced by DallasParser#and.
    def enterAnd(self, ctx:DallasParser.AndContext):
        pass

    # Exit a parse tree produced by DallasParser#and.
    def exitAnd(self, ctx:DallasParser.AndContext):
        pass


    # Enter a parse tree produced by DallasParser#equal.
    def enterEqual(self, ctx:DallasParser.EqualContext):
        pass

    # Exit a parse tree produced by DallasParser#equal.
    def exitEqual(self, ctx:DallasParser.EqualContext):
        pass


    # Enter a parse tree produced by DallasParser#negation.
    def enterNegation(self, ctx:DallasParser.NegationContext):
        pass

    # Exit a parse tree produced by DallasParser#negation.
    def exitNegation(self, ctx:DallasParser.NegationContext):
        pass


    # Enter a parse tree produced by DallasParser#bool.
    def enterBool(self, ctx:DallasParser.BoolContext):
        pass

    # Exit a parse tree produced by DallasParser#bool.
    def exitBool(self, ctx:DallasParser.BoolContext):
        pass


    # Enter a parse tree produced by DallasParser#simpleLogicalExpression.
    def enterSimpleLogicalExpression(self, ctx:DallasParser.SimpleLogicalExpressionContext):
        pass

    # Exit a parse tree produced by DallasParser#simpleLogicalExpression.
    def exitSimpleLogicalExpression(self, ctx:DallasParser.SimpleLogicalExpressionContext):
        pass


    # Enter a parse tree produced by DallasParser#add.
    def enterAdd(self, ctx:DallasParser.AddContext):
        pass

    # Exit a parse tree produced by DallasParser#add.
    def exitAdd(self, ctx:DallasParser.AddContext):
        pass


    # Enter a parse tree produced by DallasParser#singleValue3.
    def enterSingleValue3(self, ctx:DallasParser.SingleValue3Context):
        pass

    # Exit a parse tree produced by DallasParser#singleValue3.
    def exitSingleValue3(self, ctx:DallasParser.SingleValue3Context):
        pass


    # Enter a parse tree produced by DallasParser#substract.
    def enterSubstract(self, ctx:DallasParser.SubstractContext):
        pass

    # Exit a parse tree produced by DallasParser#substract.
    def exitSubstract(self, ctx:DallasParser.SubstractContext):
        pass


    # Enter a parse tree produced by DallasParser#singleValue2.
    def enterSingleValue2(self, ctx:DallasParser.SingleValue2Context):
        pass

    # Exit a parse tree produced by DallasParser#singleValue2.
    def exitSingleValue2(self, ctx:DallasParser.SingleValue2Context):
        pass


    # Enter a parse tree produced by DallasParser#divide.
    def enterDivide(self, ctx:DallasParser.DivideContext):
        pass

    # Exit a parse tree produced by DallasParser#divide.
    def exitDivide(self, ctx:DallasParser.DivideContext):
        pass


    # Enter a parse tree produced by DallasParser#multiply.
    def enterMultiply(self, ctx:DallasParser.MultiplyContext):
        pass

    # Exit a parse tree produced by DallasParser#multiply.
    def exitMultiply(self, ctx:DallasParser.MultiplyContext):
        pass


    # Enter a parse tree produced by DallasParser#singleValue1.
    def enterSingleValue1(self, ctx:DallasParser.SingleValue1Context):
        pass

    # Exit a parse tree produced by DallasParser#singleValue1.
    def exitSingleValue1(self, ctx:DallasParser.SingleValue1Context):
        pass


    # Enter a parse tree produced by DallasParser#positive.
    def enterPositive(self, ctx:DallasParser.PositiveContext):
        pass

    # Exit a parse tree produced by DallasParser#positive.
    def exitPositive(self, ctx:DallasParser.PositiveContext):
        pass


    # Enter a parse tree produced by DallasParser#negative.
    def enterNegative(self, ctx:DallasParser.NegativeContext):
        pass

    # Exit a parse tree produced by DallasParser#negative.
    def exitNegative(self, ctx:DallasParser.NegativeContext):
        pass


    # Enter a parse tree produced by DallasParser#singleValue.
    def enterSingleValue(self, ctx:DallasParser.SingleValueContext):
        pass

    # Exit a parse tree produced by DallasParser#singleValue.
    def exitSingleValue(self, ctx:DallasParser.SingleValueContext):
        pass


    # Enter a parse tree produced by DallasParser#paren.
    def enterParen(self, ctx:DallasParser.ParenContext):
        pass

    # Exit a parse tree produced by DallasParser#paren.
    def exitParen(self, ctx:DallasParser.ParenContext):
        pass


    # Enter a parse tree produced by DallasParser#toint.
    def enterToint(self, ctx:DallasParser.TointContext):
        pass

    # Exit a parse tree produced by DallasParser#toint.
    def exitToint(self, ctx:DallasParser.TointContext):
        pass


    # Enter a parse tree produced by DallasParser#tofloat.
    def enterTofloat(self, ctx:DallasParser.TofloatContext):
        pass

    # Exit a parse tree produced by DallasParser#tofloat.
    def exitTofloat(self, ctx:DallasParser.TofloatContext):
        pass


    # Enter a parse tree produced by DallasParser#value.
    def enterValue(self, ctx:DallasParser.ValueContext):
        pass

    # Exit a parse tree produced by DallasParser#value.
    def exitValue(self, ctx:DallasParser.ValueContext):
        pass


    # Enter a parse tree produced by DallasParser#dataType.
    def enterDataType(self, ctx:DallasParser.DataTypeContext):
        pass

    # Exit a parse tree produced by DallasParser#dataType.
    def exitDataType(self, ctx:DallasParser.DataTypeContext):
        pass



del DallasParser