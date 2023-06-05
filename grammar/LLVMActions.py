import enum
import sys
from collections import deque
from LLVMGenerator import LLVMGenerator
from DallasListener import DallasListener
from DallasParser import DallasParser

class VarType(enum.Enum):
    ID = 1
    INT = 2
    FLOAT = 3
    STRING = 4
    BOOLEAN = 5
    ARRAY = 6
    UNKNOWN = 7

class Value:
    def __init__(self, name, type, length):
        self.name = name
        self.type = type
        self.length = 0
        if length is not None:
            self.length = length

    def __str__(self):
        return f'Value: {self.type} = '+ f'{self.name}'

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


    # Exit a parse tree produced by DallasParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:DallasParser.VariableDeclarationContext):
        ID = ctx.ID().getText()
        if ctx.dataType().INT_KEY() is not None:
            self.local_vars[ID] = Value(ID, VarType.INT, 0);
            LLVMGenerator.declare_i32(ID);
        if ctx.dataType().FLOAT_KEY() is not None:
            self.local_vars[ID] = Value(ID, VarType.FLOAT, 0);
            LLVMGenerator.declare_double(ID);
        if ctx.dataType().STRING_KEY() is not None:
            self.local_vars[ID] = Value(ID, VarType.STRING, 0);
            LLVMGenerator.declare_string(ID);
        if ctx.dataType().ARRAY_KEY() is not None:
            self.local_vars[ID] = Value(ID, VarType.ARRAY, 0);
            LLVMGenerator.declare_array(ID);
        if ctx.dataType().BOOL_KEY() is not None:
            self.local_vars[ID] = Value(ID, VarType.BOOLEAN, 0);
            LLVMGenerator.declare_bool(ID);

    # Exit a parse tree produced by DallasParser#printCall.
    def exitPrintCall(self, ctx:DallasParser.PrintCallContext):
        ID = ctx.ID()
        if ID is not None:
            ID = ID.getText()
            v = self.local_vars.get(ID)
            if v is not None:
                if v.type == VarType.INT:
                    LLVMGenerator.printf_i32(self.set_variable(ID, v))
                if v.type == VarType.FLOAT:
                    LLVMGenerator.printf_double(self.set_variable(ID, v))
                if v.type == VarType.STRING:
                    LLVMGenerator.printf_string(self.set_variable(ID, v))
                if v.type == VarType.BOOLEAN:
                    LLVMGenerator.printf_string(self.set_variable(ID, v))
        else:
            error(ctx.getRuleIndex(), f"unknown variable {ID}")

    # Exit a parse tree produced by DallasParser#readCall.
    def exitReadCall(self, ctx:DallasParser.ReadCallContext):
        ID = ctx.ID().getText()
        if ID in self.local_vars:
            v = self.local_vars.get(ID)
            if v.type == VarType.INT:
                self.set_variable(ID, Value(ID, VarType.INT, 0))
                LLVMGenerator.scanf_i32("%" +ID)
            elif v.type == VarType.FLOAT:
                self.set_variable(ID, Value(ID, VarType.FLOAT, 0))
                LLVMGenerator.scanf_double("%" +ID)
        else:
            error(ctx.getRuleIndex(), f"unknown variable {ID}")



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


    # Exit a parse tree produced by DallasParser#assignment.
    def exitAssignment(self, ctx:DallasParser.AssignmentContext):
        ID = ctx.ID().getText()
        v = self.stack.pop()

        print('assign')
        print(ID)
        print(v)

        if hasattr(self.local_vars, ID):
            error(ctx.getRuleIndex(), "unknown variable ")
            return
        if v.type == VarType.INT:
            LLVMGenerator.assign_i32(self.set_variable(ID, v), v.name)
        if v.type == VarType.FLOAT:
            LLVMGenerator.assign_double(self.set_variable(ID, v), v.name)
        if v.type == VarType.STRING:
            LLVMGenerator.assign_string(self.set_variable(ID, v))
        if v.type == VarType.BOOLEAN:
            LLVMGenerator.assign_bool(self.set_variable(ID, v), v.name)
        if v.type == VarType.ARRAY:
            LLVMGenerator.assign_array(self.set_variable(ID, v), v.name)
        if v.type == VarType.UNKNOWN:
            error(ctx.getRuleIndex(), "unknown variable " + ID)
            return


    # Exit a parse tree produced by DallasParser#expression.
    def exitExpression(self, ctx:DallasParser.ExpressionContext):
        pass
        # next if with logical expressions

    # Exit a parse tree produced by DallasParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:DallasParser.AdditiveExpressionContext):
        print("ctx:");
        print(ctx);
        print("stack:")
        v1 = self.stack.pop()
        print(v1.type);
        addition = ctx.PLUS()
        substraction = ctx.MINUS()
        print(addition);
        print(substraction);
        v2 = self.stack.pop()
        if v1.type == v2.type:
            if v1.type == VarType.INT:
                if addition is not None:
                    LLVMGenerator.add_i32(v1.name, v2.name)
                if substraction is not None:
                    LLVMGenerator.sub_i32(v1.name, v2.name)
                self.stack.push(Value(f"%{LLVMGenerator.main_tmp-1}", VarType.INT, 0))
            if v1.type == VarType.FLOAT:
                if addition is not None:
                    LLVMGenerator.add_double(v1.name, v2.name)
                if substraction is not None:
                    LLVMGenerator.sub_double(v1.name, v2.name)
                self.stack.push(Value(f"%{LLVMGenerator.main_tmp-1}", VarType.FLOAT, 0))
        else:
            if addition is not None:
                error(ctx.getRuleIndex(), "addition type mismatch")
            if substraction is not None:
                error(ctx.getRuleIndex(), "substraction type mismatch")


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
                self.stack.push(Value(f"%{LLVMGenerator.main_tmp-1}", VarType.INT, 0))
            if v1.type == VarType.FLOAT:
                if multiplication is not None:
                    LLVMGenerator.mul_double(v1.name, v2.name)
                if division is not None:
                    LLVMGenerator.div_double(v1.name, v2.name)
                self.stack.push(Value(f"%{LLVMGenerator.main_tmp-1}", VarType.FLOAT, 0))
        else:
            if multiplication is not None:
                error(ctx.getRuleIndex(), "multiplication type mismatch")
            if division is not None:
                error(ctx.getRuleIndex(), "division type mismatch")


    # Exit a parse tree produced by DallasParser#unaryExpression.
    def exitUnaryExpression(self, ctx:DallasParser.UnaryExpressionContext):
        pass


    # Exit a parse tree produced by DallasParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:DallasParser.PrimaryExpressionContext):
        # todo: IMPLEMENT THIS
        print(ctx)
        if ctx.LPAREN() and ctx.RPAREN is True :
            pass
        if ctx.toInt() is not None:
            v = self.stack.pop();
            LLVMGenerator.fptosi(v.name);
            self.stack.append(Value(f"%{LLVMGenerator.reg-1}", VarType.INT, 0))
        if ctx.toFloat() is not None:
            LLVMGenerator.sitofp(v.name);
            self.stack.append(Value(f"%{LLVMGenerator.reg-1}", VarType.FLOAT, 0))
        pass

    # def exitEqual(self, ctx):
    #     ID = ctx.ID()
    #     INT = ctx.INT()
    #     LLVMGenerator.icmp(self.set_variable(ID, VarType.INT), INT)

    def exitValue(self, ctx:DallasParser.ValueContext):
        print('value')
        if ctx.ID() is not None:
            ID = ctx.ID().getText()
            if ID in self.local_vars:
                v = self.local_vars.get(ID)
                loadType(v.type, "%" + ID)
                self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), v.type, v.length));
            else:
                print(ID)
                error(ctx.getRuleIndex(), f"unknown variable {ID}")

        if ctx.INT() is not None:
            self.stack.append(Value(ctx.INT().getText(), VarType.INT, 0))
        if ctx.FLOAT() is not None:
            self.stack.append(Value(ctx.FLOAT().getText(), VarType.FLOAT, 0))
        if ctx.STRING() is not None:
            tmp = ctx.STRING().getText();
            print('string value:'+ tmp)
            self.stack.append(Value(ctx.STRING().getText(), VarType.STRING, 0))
        if ctx.BOOL() is not None:
            self.stack.append(Value(ctx.BOOL().getText(), VarType.BOOLEAN, 0))


    def set_variable(self, ID, value):
        if ID not in self.local_vars:
            self.local_vars[ID] = value
            declareType(value, ID)
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
    if type == "BOOL":
        LLVMGenerator.declare_bool(ID, False)

def loadType(type, msg):
    if type == VarType.INT:
        LLVMGenerator.load_i32(msg)
    if type == VarType.FLOAT:
        LLVMGenerator.load_double(msg)
    if type == VarType.STRING:
        LLVMGenerator.load_string(msg)
    if type == VarType.ARRAY:
        LLVMGenerator.load_array(msg)
    if type == VarType.BOOLEAN:
        LLVMGenerator.load_bool(msg)
