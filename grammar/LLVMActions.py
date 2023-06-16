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
        self.global_vars = {}
        self.stack = deque()
        self.global_ = None


    # Enter a parse tree produced by DallasParser#prog.
    def enterProg(self, ctx:DallasParser.ProgContext):
        self.global_ = True


    # Exit a parse tree produced by DallasParser#prog.
    def exitProg(self, ctx):
        LLVMGenerator.close_main()
        with open("output.ll", "w") as file:
            file.write(LLVMGenerator.generate())
        print(LLVMGenerator.generate())


    # Exit a parse tree produced by DallasParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:DallasParser.VariableDeclarationContext):
        ID = ctx.ID().getText()
        if ctx.dataType().INT_KEY() is not None:
            v = Value(ID, VarType.INT, 0)
        if ctx.dataType().FLOAT_KEY() is not None:
            v = Value(ID, VarType.FLOAT, 0)
        if ctx.dataType().STRING_KEY() is not None:
            v = Value(ID, VarType.STRING, 0)
        if ctx.dataType().ARRAY_KEY() is not None:
            v = Value(ID, VarType.ARRAY, 0)
        if ctx.dataType().BOOL_KEY() is not None:
            v = Value(ID, VarType.BOOLEAN, 0)
        if v is None:
            error(ctx.getRuleIndex(), 'wrong type')
        setVariable(self, ID, v)
        

    # Exit a parse tree produced by DallasParser#printCall.
    def exitPrintCall(self, ctx:DallasParser.PrintCallContext):
        ID = ctx.ID()
        if ID is not None:
            ID = ID.getText()
            scopedId, v = getVariable(self, ID, ctx.getRuleIndex())
            if v is not None:
                if v.type == VarType.INT:
                    LLVMGenerator.printf_i32(scopedId)
                if v.type == VarType.FLOAT:
                    LLVMGenerator.printf_double(scopedId)
                if v.type == VarType.STRING:
                    LLVMGenerator.printf_string(scopedId)
                if v.type == VarType.BOOLEAN:
                    LLVMGenerator.printf_string(scopedId)
            else:
                error(ctx.getRuleIndex(), f"Print unknown variable {ID}")
        else:
            error(ctx.getRuleIndex(), f"Print unknown variable {ID}")

    # Exit a parse tree produced by DallasParser#readCall.
    def exitReadCall(self, ctx:DallasParser.ReadCallContext):
        ID = ctx.ID().getText()
        scopedId, v = getVariable(self, ID, ctx.getRuleIndex())

        if v.type == VarType.INT:
            LLVMGenerator.scanf_i32(scopedId)
        elif v.type == VarType.FLOAT:
            LLVMGenerator.scanf_double(scopedId)
        else:
            error(ctx.getRuleIndex(), f"unknown variable type {ID}")


    # Exit a parse tree produced by DallasParser#assignment.
    def exitAssignment(self, ctx:DallasParser.AssignmentContext):
        ID = ctx.ID().getText()
        v = self.stack.pop()
        scopedId, value = getVariable(self, ID, ctx.getRuleIndex())
        if v.type == VarType.INT:
            LLVMGenerator.assign_i32(setVariable(self, ID, v), v.name)
        if v.type == VarType.FLOAT:
            LLVMGenerator.assign_double(setVariable(self, ID, v), v.name)
        if v.type == VarType.STRING:
            LLVMGenerator.assign_string(setVariable(self, ID, v))
        if v.type == VarType.BOOLEAN:
            LLVMGenerator.assign_bool(setVariable(self, ID, v), v.name)
        if v.type == VarType.ARRAY:
            LLVMGenerator.assign_array(setVariable(self, ID, v), v.name)
        if v.type == VarType.UNKNOWN:
            error(ctx.getRuleIndex(), "Assignment unknown variable " + ID)

    # Exit a parse tree produced by DallasParser#add.
    # Exit a parse tree produced by DallasParser#add.
    def exitAdd(self, ctx:DallasParser.AddContext):
        v1 = self.stack.pop()
        v2 = self.stack.pop()
        if (v1.type == VarType.INT and v2.type == VarType.INT):
            LLVMGenerator.add_i32(v1.name, v2.name)
            self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), VarType.INT, 0))
        elif (v1.type == VarType.FLOAT and v2.type == VarType.FLOAT):
            LLVMGenerator.add_double(v1.name,v2.name)
            self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), VarType.FLOAT, 0))
        elif ((v1.type == VarType.INT and v2.type == VarType.FLOAT) or 
            (v1.type == VarType.FLOAT and v2.type == VarType.INT)):
            # For the case when one value is an integer and the other is a float,
            # we will convert the integer to float and then add
            if v1.type == VarType.INT:
                LLVMGenerator.sitofp(v1.name)  # convert int to float
                v1.name = f"%{LLVMGenerator.reg - 1}"
                v1.type = VarType.FLOAT
            else:
                LLVMGenerator.sitofp(v2.name)  # convert int to float
                v2.name = f"%{LLVMGenerator.reg - 1}"
                v2.type = VarType.FLOAT
            LLVMGenerator.add_double(v1.name,v2.name)
            self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), VarType.FLOAT, 0))
        else:
            error(ctx.getRuleIndex(), "invalid operand types for addition operation")

    # Exit a parse tree produced by DallasParser#substract.
    def exitSubstract(self, ctx:DallasParser.SubstractContext):
        v1 = self.stack.pop()
        v2 = self.stack.pop()
        if (v1.type == VarType.INT and v2.type == VarType.INT):
            LLVMGenerator.sub_i32(v1.name, v2.name)
            self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), VarType.INT, 0))
        elif (v1.type == VarType.FLOAT and v2.type == VarType.FLOAT):
            LLVMGenerator.sub_double(v1.name,v2.name)
            self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), VarType.FLOAT, 0))
        elif ((v1.type == VarType.INT and v2.type == VarType.FLOAT) or 
            (v1.type == VarType.FLOAT and v2.type == VarType.INT)):
            # For the case when one value is an integer and the other is a float,
            # we will convert the integer to float and then subtract
            if v1.type == VarType.INT:
                LLVMGenerator.sitofp(v1.name)  # convert int to float
                v1.name = f"%{LLVMGenerator.reg - 1}"
                v1.type = VarType.FLOAT
            else:
                LLVMGenerator.sitofp(v2.name)  # convert int to float
                v2.name = f"%{LLVMGenerator.reg - 1}"
                v2.type = VarType.FLOAT
            LLVMGenerator.sub_double(v1.name,v2.name)
            self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), VarType.FLOAT, 0))
        else:
            error(ctx.getRuleIndex(), "invalid operand types for subtraction operation")

    # Exit a parse tree produced by DallasParser#multiply.
    def exitMultiply(self, ctx:DallasParser.MultiplyContext):
        v1 = self.stack.pop()
        v2 = self.stack.pop()
        if (v1.type == VarType.INT and v2.type == VarType.INT):
            LLVMGenerator.mul_i32(v1.name, v2.name)
            self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), VarType.INT, 0))
        elif (v1.type == VarType.FLOAT and v2.type == VarType.FLOAT):
            LLVMGenerator.mul_double(v1.name,v2.name)
            self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), VarType.FLOAT, 0))
        elif ((v1.type == VarType.INT and v2.type == VarType.FLOAT) or 
            (v1.type == VarType.FLOAT and v2.type == VarType.INT)):
            # For the case when one value is an integer and the other is a float,
            # we will convert the integer to float and then multiply
            if v1.type == VarType.INT:
                LLVMGenerator.sitofp(v1.name)  # convert int to float
                v1.name = f"%{LLVMGenerator.reg - 1}"
                v1.type = VarType.FLOAT
            else:
                LLVMGenerator.sitofp(v2.name)  # convert int to float
                v2.name = f"%{LLVMGenerator.reg - 1}"
                v2.type = VarType.FLOAT
            LLVMGenerator.mul_double(v1.name,v2.name)
            self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), VarType.FLOAT, 0))
        else:
            error(ctx.getRuleIndex(), "invalid operand types for multiplication operation")

    # Exit a parse tree produced by DallasParser#divide.
    def exitDivide(self, ctx:DallasParser.DivideContext):
        v1 = self.stack.pop()
        v2 = self.stack.pop()
        if (v1.type == VarType.INT and v2.type == VarType.INT):
            LLVMGenerator.div_i32(v1.name, v2.name)
            self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), VarType.INT, 0))
        elif (v1.type == VarType.FLOAT and v2.type == VarType.FLOAT):
            LLVMGenerator.div_double(v1.name,v2.name)
            self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), VarType.FLOAT, 0))
        elif ((v1.type == VarType.INT and v2.type == VarType.FLOAT) or 
            (v1.type == VarType.FLOAT and v2.type == VarType.INT)):
            # For the case when one value is an integer and the other is a float,
            # we will convert the integer to float and then divide
            if v1.type == VarType.INT:
                LLVMGenerator.sitofp(v1.name)  # convert int to float
                v1.name = f"%{LLVMGenerator.reg - 1}"
                v1.type = VarType.FLOAT
            else:
                LLVMGenerator.sitofp(v2.name)  # convert int to float
                v2.name = f"%{LLVMGenerator.reg - 1}"
                v2.type = VarType.FLOAT
            LLVMGenerator.div_double(v1.name,v2.name)
            self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), VarType.FLOAT, 0))
        else:
            error(ctx.getRuleIndex(), "invalid operand types for division operation")


    # Exit a parse tree produced by DallasParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:DallasParser.PrimaryExpressionContext):
        # todo: IMPLEMENT THIS
        print(ctx)
        if ctx.LPAREN() and ctx.RPAREN is True :
            pass
        if ctx.toInt() is not None:
            v = self.stack.pop()
            LLVMGenerator.fptosi(v.name)
            self.stack.append(Value(f"%{LLVMGenerator.reg-1}", VarType.INT, 0))
        if ctx.toFloat() is not None:
            LLVMGenerator.sitofp(v.name)
            self.stack.append(Value(f"%{LLVMGenerator.reg-1}", VarType.FLOAT, 0))
        pass

    # def exitEqual(self, ctx):
    #     ID = ctx.ID()
    #     INT = ctx.INT()
    #     LLVMGenerator.icmp(setVariable(self, ID, VarType.INT), INT)

    def compare(self, ctx, comparison, fcomparison):
        ve1 = ctx.ID().getText()
        ve2 = ctx.value()
        scopedId1, v1 = getVariable(self, ve1, ctx.getRuleIndex())
        if ve2.ID() is not None:
            scopedId2, v2 = getVariable(self, ve2.name, ctx.getRuleIndex())
            if v2.INT() is not None:
                LLVMGenerator.icmp_id(scopedId1, scopedId2, comparison)
            elif v2.FLOAT() is not None:
                LLVMGenerator.fcmp_id(scopedId1, scopedId2, fcomparison)
            else:
                error(ctx.getRuleIndex(), 'wrong type comparison')
        elif v1.type == VarType.INT and ve2.INT() is not None:
            LLVMGenerator.icmp(scopedId1, ve2.INT().getText(), comparison)
        elif v1.type == VarType.FLOAT and ve2.FLOAT() is not None:
            LLVMGenerator.fcmp(scopedId1, ve2.FLOAT().getText(), fcomparison)
        else:
            error(ctx.getRuleIndex(), 'wrong type comparison')
    
    # Exit a parse tree produced by DallasParser#isEqual.
    def exitIsEqual(self, ctx:DallasParser.IsEqualContext):
        comparison = 'eq'
        fcomparison = 'oeq'
        self.compare(ctx, comparison, fcomparison)

    # Exit a parse tree produced by DallasParser#notEqual.
    def exitNotEqual(self, ctx:DallasParser.NotEqualContext):
        comparison = 'ne'
        fcomparison = 'one'
        self.compare(ctx, comparison, fcomparison)

    # Exit a parse tree produced by DallasParser#lesserThan.
    def exitLesserThan(self, ctx:DallasParser.LesserThanContext):
        comparison = 'ult'
        fcomparison = 'olt'
        self.compare(ctx, comparison, fcomparison)

    # Exit a parse tree produced by DallasParser#lesserThanEqual.
    def exitLesserThanEqual(self, ctx:DallasParser.LesserThanEqualContext):
        comparison = 'ule'
        fcomparison = 'ole'
        self.compare(ctx, comparison, fcomparison)

    # Exit a parse tree produced by DallasParser#greaterThan.
    def exitGreaterThan(self, ctx:DallasParser.GreaterThanContext):
        comparison = 'ugt'
        fcomparison = 'ogt'
        self.compare(ctx, comparison, fcomparison)

    # Exit a parse tree produced by DallasParser#greaterThanEqual.
    def exitGreaterThanEqual(self, ctx:DallasParser.GreaterThanEqualContext):
        comparison = 'uge'
        fcomparison = 'oge'
        self.compare(ctx, comparison, fcomparison)

    # Exit a parse tree produced by DallasParser#toInt.
    def exitToInt(self, ctx:DallasParser.ToIntContext):
        v = self.stack.pop()
        LLVMGenerator.fptosi(v.name)
        self.stack.append(Value(f"%{LLVMGenerator.reg - 1}", VarType.INT))

    
    # Exit a parse tree produced by DallasParser#toFloat.
    def exitToFloat(self, ctx:DallasParser.ToFloatContext):
        v = self.stack.pop()
        LLVMGenerator.sitofp(v.name)
        self.stack.append(Value(f"%{LLVMGenerator.reg - 1}", VarType.FLOAT))


    def exitValue(self, ctx:DallasParser.ValueContext):
        if ctx.ID() is not None:
            ID = ctx.ID().getText()
            scopedId, v = getVariable(self, ID, ctx.getRuleIndex())
            loadType(v.type, scopedId)
            self.stack.append(Value(ID, v.type, v.length))

        if ctx.INT() is not None:
            self.stack.append(Value(ctx.INT().getText(), VarType.INT, 0))
        if ctx.FLOAT() is not None:
            self.stack.append(Value(ctx.FLOAT().getText(), VarType.FLOAT, 0))
        if ctx.STRING() is not None:
            self.stack.append(Value(ctx.STRING().getText(), VarType.STRING, 0))
        if ctx.BOOL() is not None:
            self.stack.append(Value(ctx.BOOL().getText(), VarType.BOOLEAN, 0))

    # Enter a parse tree produced by DallasParser#ifBlock.
    def enterIfBlock(self, ctx:DallasParser.IfBlockContext):
        LLVMGenerator.ifstart()

    # Exit a parse tree produced by DallasParser#ifBlock.
    def exitIfBlock(self, ctx:DallasParser.IfBlockContext):
        LLVMGenerator.ifend()

    # Exit a parse tree produced by DallasParser#repetitions.
    def exitRepetitions(self, ctx:DallasParser.RepetitionsContext):
        int = ctx.INT()
        if int is not None:
            LLVMGenerator.loopstart(int)
        else:
            error(ctx.getRuleIndex, 'wrong number')

    # Exit a parse tree produced by DallasParser#loopBlock.
    def exitLoopBlock(self, ctx:DallasParser.LoopBlockContext):
        if isinstance(ctx.parentCtx, DallasParser.LoopTimesContext):
            LLVMGenerator.loopend()

def error(line, msg):
    print("Error, line " + str(line) + ", " + msg, file=sys.stderr)
    sys.exit(1)

def declareType(type, ID, isGlobal = False):
    if type == "INT":
        LLVMGenerator.declare_i32(ID, isGlobal)
    if type == "FLOAT":
        LLVMGenerator.declare_double(ID, isGlobal)
    if type == "STRING":
        LLVMGenerator.declare_string(ID, isGlobal)
    if type == "ARRAY":
        LLVMGenerator.declare_array(ID, isGlobal)
    if type == "BOOL":
        LLVMGenerator.declare_bool(ID, isGlobal)

# todo: change all those load generators to take ID, this ID already has scope in it
def loadType(type, scopedID):
    if type == VarType.INT:
        LLVMGenerator.load_i32(scopedID)
    if type == VarType.FLOAT:
        LLVMGenerator.load_double(scopedID)
    if type == VarType.STRING:
        LLVMGenerator.load_string(scopedID)
    if type == VarType.ARRAY:
        LLVMGenerator.load_array(scopedID)
    if type == VarType.BOOLEAN:
        LLVMGenerator.load_bool(scopedID)

def getVariable(self, ID, line):
    if self.global_:
        if ID in self.global_vars:
            return "@" + ID, self.global_vars[ID]
        else:
            error(line, "getVariable unknown global variable " + ID)
    else:
        if ID in self.local_vars:
            return "%" + ID, self.local_vars[ID]
        elif ID in self.global_vars:
            return "@" + ID, self.global_vars[ID]
        else:
            error(line, "getVariable unknown variable " + ID)

# sprawdź context, zapisz w local/global, zwróć scoped id
def setVariable(self, ID, value):
    if self.global_:
        if ID not in self.global_vars:
            declareType(value.type, ID, True)
        self.global_vars[ID] = value
        scopedID = "@" + ID
    else:
        if ID not in self.local_vars:
            declareType(value.type, ID, False)
        self.local_vars[ID] = value
        scopedID = "%" + ID

    return scopedID
