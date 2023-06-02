import enum
from collections import deque

from LLVMGenerator import LLVMGenerator
from DallasListener import DallasListener
from DallasParser import DallasParser

class VarType(enum.Enum):
    ID = 1
    INT = 2
    FLOAT = 3
    STRING = 4
    ARRAY = 5
    UNKNOWN = 6

class Value:
    def __init__(self, name, type, length):
        self.name = name
        self.type = type
        self.length = length

class LLVMActions(DallasListener):
    def __init__(self):
        self.local_vars = {}
        self.stack = deque()
        self.global_ = None


    # Enter a parse tree produced by DallasParser#prog.
    def enterProg(self, ctx:DallasParser.ProgContext):
        self.global_ = True


    # Exit a parse tree produced by DallasParser#prog.
    def exitProg(self, ctx):
        LLVMGenerator.close_main()
        print(LLVMGenerator.generate())

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
        ID = ctx.ID().getText()
        if ctx.dataType().INT_KEY() is not None:
            LLVMGenerator.declare_i32(ID);
            self.stack.append(Value("%" + str(LLVMGenerator.main_tmp - 1), VarType.ID, 1))
        if ctx.dataType().FLOAT_KEY() is not None:
            LLVMGenerator.declare_double(ID);
            self.stack.append(Value("%" + str(LLVMGenerator.main_tmp - 1), VarType.ID, 1))
        if ctx.dataType().STRING_KEY() is not None:
            LLVMGenerator.declare_string(ID);
            self.stack.append(Value("%" + str(LLVMGenerator.main_tmp - 1), VarType.ID, 64))
        if ctx.dataType().ARRAY_KEY() is not None:
            LLVMGenerator.declare_array(ID);
            self.stack.append(Value("%" + str(LLVMGenerator.main_tmp - 1), VarType.ID, 64))


    # Enter a parse tree produced by DallasParser#printCall.
    def enterPrintCall(self, ctx:DallasParser.PrintCallContext):
        pass

    # Exit a parse tree produced by DallasParser#printCall.
    def exitPrintCall(self, ctx:DallasParser.PrintCallContext):
        ID = ctx.ID().getText()
        type = local_vars.get(ID)
        if type is not None:
            if type == VarType.INT:
                LLVMGenerator.printf_i32(set_variable(ID, type))
            if type == VarType.FLOAT:
                LLVMGenerator.printf_double(set_variable(ID, type))
            if type == VarType.STRING:
                LLVMGenerator.printf_string(set_variable(ID, type))
            if type == VarType.ARRAY:
                LLVMGenerator.printf_array(set_variable(ID, type))
        else:
            error(ctx.getStart().getLine(), f"unknown variable {ID}")


    # Enter a parse tree produced by DallasParser#readCall.
    def enterReadCall(self, ctx:DallasParser.ReadCallContext):
        pass

    # Exit a parse tree produced by DallasParser#readCall.
    def exitReadCall(self, ctx:DallasParser.ReadCallContext):
        ID = ctx.ID().getText()
        LLVMGenerator.scanf(set_variable(ID, VarType.INT))


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
        ID = ctx.ID().getText()
        v = self.stack.pop()

        if v.type == VarType.INT:
            LLVMGenerator.assign_i32(self.set_variable(ID, v.type), v.name)
        if v.type == VarType.FLOAT:
            LLVMGenerator.assign_double(self.set_variable(ID, v.type), v.name)
        if v.type == VarType.STRING:
            LLVMGenerator.assign_string(self.set_variable(ID, v.type), v.name)
        if v.type == VarType.ARRAY:
            LLVMGenerator.assign_array(self.set_variable(ID, v.type), v.name)
        if v.type == VarType.UNKNOWN:
            self.error(ctx.getStart().getLine(), "unknown variable " + ID)


    # Enter a parse tree produced by DallasParser#expression.
    def enterExpression(self, ctx:DallasParser.ExpressionContext):
        pass

    # Exit a parse tree produced by DallasParser#expression.
    def exitExpression(self, ctx:DallasParser.ExpressionContext):
        if ctx.ID() is not None:
            ID = ctx.ID().getText()
            if ID in self.local_vars:
                type = self.local_vars.get(ID)
                self.loadType(type, "%" + ID)
            else:
                self.error(ctx.getStart().getLine(), "Unknown local variable" + ID)

        if ctx.INT() is not None:
            self.exitInt(self, ctx)
        if ctx.FLOAT() is not None:
            self.exitFloat(self, ctx)
        if ctx.STRING() is not None:
            self.exitString(self, ctx)
        if ctx.array() is not None:
            self.exitArray(self, ctx)
        # next if with logical expressions


    # Enter a parse tree produced by DallasParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:DallasParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by DallasParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:DallasParser.AdditiveExpressionContext):
        v1 = self.stack.pop()
        v2 = self.stack.pop()
        addition = ctx.PLUS()
        substraction = ctx.MINUS()
        if v1.type == v2.type:
            if v1.type == VarType.INT:
                if addition is not None:
                    LLVMGenerator.add_i32(v1.name, v2.name)
                if substraction is not None:
                    LLVMGenerator.sub_i32(v1.name, v2.name)
                self.stack.push(Value(f"%{LLVMGenerator.main_tmp-1}", VarType.INT))
            if v1.type == VarType.REAL:
                if addition is not None:
                    LLVMGenerator.add_double(v1.name, v2.name)
                if substraction is not None:
                    LLVMGenerator.sub_double(v1.name, v2.name)
                self.stack.push(Value(f"%{LLVMGenerator.main_tmp-1}", VarType.FLOAT))
        else:
            if addition is not None:
                error(ctx.getStart().getLine(), "addition type mismatch")
            if substraction is not None:
                error(ctx.getStart().getLine(), "substraction type mismatch")


    # Enter a parse tree produced by DallasParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:DallasParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by DallasParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:DallasParser.MultiplicativeExpressionContext):
        v1 = self.stack.pop()
        v2 = self.stack.pop()
        multiplication = ctx.ASTERISK()
        division = ctx.SLASH()
        if v1.type == v2.type:
            if v1.type == VarType.INT:
                if multiplication is not None:
                    LLVMGenerator.mul_i32(v1.name, v2.name)
                if division is not None:
                    LLVMGenerator.div_i32(v1.name, v2.name)
                self.stack.push(Value(f"%{LLVMGenerator.main_tmp-1}", VarType.INT))
            if v1.type == VarType.FLOAT:
                if multiplication is not None:
                    LLVMGenerator.mul_double(v1.name, v2.name)
                if division is not None:
                    LLVMGenerator.div_double(v1.name, v2.name)
                self.stack.push(Value(f"%{LLVMGenerator.main_tmp-1}", VarType.FLOAT))
        else:
            if multiplication is not None:
                error(ctx.getStart().getLine(), "multiplication type mismatch")
            if division is not None:
                error(ctx.getStart().getLine(), "division type mismatch")


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

    # def exitEqual(self, ctx):
    #     ID = ctx.ID().getText()
    #     INT = ctx.INT().getText()
    #     LLVMGenerator.icmp(self.set_variable(ID, VarType.INT), INT)

    def exitInt(self, ctx):
        self.stack.append(Value(ctx.INT().getText(), VarType.INT))

    def exitFloat(self, ctx):
        self.stack.append(Value(ctx.FLOAT().getText(), VarType.FLOAT))

    def exitString(self, ctx):
        self.stack.append(Value(ctx.STRING().getText(), VarType.STRING))

    def exitArray(self, ctx):
        self.stack.append(Value(ctx.ARRAY().getText(), VarType.ARRAY))
    
    # def exitToint(self, ctx:DallasParser.TointContext):
    #     v = self.stack.pop()
    #     LLVMGenerator.fptosi(v.name)
    #     self.stack.push(Value(f"%{LLVMGenerator.main_tmp-1}", VarType.INT))
    
    # def exitToreal(self, ctx:DallasParser.TorealContext):
    #     v = self.stack.pop()
    #     LLVMGenerator.sitofp(v.name)
    #     self.stack.push(Value(f"%{LLVMGenerator.main_tmp-1}", VarType.REAL))

    # def exitCall(self, ctx:DallasParser.CallContext):
    #     LLVMGenerator.call(ctx.ID().getText())
    
    def set_variable(ID, TYPE):
        if ID not in local_vars:
            local_vars[ID] = TYPE
            declareType(TYPE, ID)
        id = "%" + ID
        return id

def error(line, msg):
    print("Error, line " + str(line) + ", " + msg, file=sys.stderr)
    sys.exit(1)

def declareType(type, ID):
    if type == "INT":
        LLVMGenerator.declare_i32(ID, False)
    if type == "FLOAT":
        LLVMGenerator.declare_double(ID, False)
    if type == "STRING":
        LLVMGenerator.declare_string(ID, False)
    if type == "ARRAY":
        LLVMGenerator.declare_array(ID, False)

def loadType(type, msg):
    if type == VarType.INT:
        LLVMGenerator.load_i32(msg)
    if type == VarType.FLOAT:
        LLVMGenerator.load_double(msg)
    if type == VarType.STRING:
        LLVMGenerator.load_string(msg)
    if type == VarType.ARRAY:
        LLVMGenerator.load_array(msg)
