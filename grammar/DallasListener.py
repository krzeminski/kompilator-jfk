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


    # Enter a parse tree produced by DallasParser#assignment.
    def enterAssignment(self, ctx:DallasParser.AssignmentContext):
        pass

    # Exit a parse tree produced by DallasParser#assignment.
    def exitAssignment(self, ctx:DallasParser.AssignmentContext):
        pass


    # Enter a parse tree produced by DallasParser#expression.
    def enterExpression(self, ctx:DallasParser.ExpressionContext):
        pass

    # Exit a parse tree produced by DallasParser#expression.
    def exitExpression(self, ctx:DallasParser.ExpressionContext):
        pass


    # Enter a parse tree produced by DallasParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:DallasParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by DallasParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:DallasParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by DallasParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:DallasParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by DallasParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:DallasParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by DallasParser#unaryExpression.
    def enterUnaryExpression(self, ctx:DallasParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by DallasParser#unaryExpression.
    def exitUnaryExpression(self, ctx:DallasParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by DallasParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:DallasParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by DallasParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:DallasParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by DallasParser#dataType.
    def enterDataType(self, ctx:DallasParser.DataTypeContext):
        pass

    # Exit a parse tree produced by DallasParser#dataType.
    def exitDataType(self, ctx:DallasParser.DataTypeContext):
        pass


    # Enter a parse tree produced by DallasParser#mathOperator.
    def enterMathOperator(self, ctx:DallasParser.MathOperatorContext):
        pass

    # Exit a parse tree produced by DallasParser#mathOperator.
    def exitMathOperator(self, ctx:DallasParser.MathOperatorContext):
        pass



del DallasParser