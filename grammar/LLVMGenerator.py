class LLVMGenerator:
    header_text = ""
    main_text = ""
    main_tmp = 1
    reg = 1
    br = 0
    brstack = []
    buffer = ""

    @staticmethod
    def funkcjastart(id):
        LLVMGenerator.main_text += LLVMGenerator.buffer
        LLVMGenerator.main_tmp = LLVMGenerator.reg
        LLVMGenerator.buffer = f"define i32 @{id}() nounwind {{\n"
        LLVMGenerator.reg = 1

    @staticmethod
    def funkcjaend():
        LLVMGenerator.buffer += f"ret i32 %{LLVMGenerator.reg-1}\n"
        LLVMGenerator.buffer += "}\n"
        LLVMGenerator.header_text += LLVMGenerator.buffer
        LLVMGenerator.buffer = ""
        LLVMGenerator.reg = LLVMGenerator.main_tmp

    @staticmethod
    def icmp(id,value):
        LLVMGenerator.buffer += f"%{LLVMGenerator.reg} = load i32, i32* {id}\n"
        LLVMGenerator.reg += 1
        LLVMGenerator.buffer += f"%{LLVMGenerator.reg} = icmp eq i32 %{LLVMGenerator.reg-1},{value}\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def ifstart():
        LLVMGenerator.br += 1
        LLVMGenerator.buffer += f"br i1 %{LLVMGenerator.reg-1}, label %true{LLVMGenerator.br}, label %false{LLVMGenerator.br}\n"
        LLVMGenerator.buffer += f"true{LLVMGenerator.br}:\n"
        LLVMGenerator.brstack.append(LLVMGenerator.br)

    
    @staticmethod
    def ifend():
        b =  LLVMGenerator.brstack.pop()
        LLVMGenerator.buffer += f"br label %false{b}\n"
        LLVMGenerator.buffer += f"false{b}:\n"

    @staticmethod  
    def repeatstart(repetitions):
        LLVMGenerator.declare_i32(str(LLVMGenerator.reg), False)
        counter = LLVMGenerator.reg
        LLVMGenerator.reg += 1
        LLVMGenerator.assign_i32(f"%{counter}", "0")
        LLVMGenerator.br += 1
        LLVMGenerator.buffer += f"br label %cond{LLVMGenerator.br}\n"
        LLVMGenerator.buffer += f"cond{LLVMGenerator.br}:\n"

        LLVMGenerator.load_i32(f"%{counter}")
        LLVMGenerator.add_i32(f"%{LLVMGenerator.reg-1}", "1")
        LLVMGenerator.assign_i32(f"%{counter}", f"%{LLVMGenerator.reg-1}")

        LLVMGenerator.buffer += f"%{LLVMGenerator.reg} = icmp slt i32 %{LLVMGenerator.reg-2}, {repetitions}\n"
        LLVMGenerator.reg += 1

        LLVMGenerator.buffer += f"br i1 %{LLVMGenerator.reg-1}, label %true{LLVMGenerator.br}, label %false{LLVMGenerator.br}\n"
        LLVMGenerator.buffer += f"true{LLVMGenerator.br}:\n"
        LLVMGenerator.brstack.append(LLVMGenerator.br)
    



    @staticmethod
    def repeatend():
        b =  LLVMGenerator.brstack.pop()
        LLVMGenerator.buffer += f"br label %cond{b}\n"
        LLVMGenerator.buffer += f"false{b}:\n"
   




    @staticmethod
    def printf_i32(id):
        LLVMGenerator.buffer += f"%{LLVMGenerator.reg} = load i32, i32* {id}\n"
        LLVMGenerator.reg += 1
        LLVMGenerator.buffer += f"%{LLVMGenerator.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %{LLVMGenerator.reg-1})\n"
        LLVMGenerator.reg += 1
    
    @staticmethod
    def printf_double(id):
        LLVMGenerator.buffer += f"%{LLVMGenerator.reg} = load double, double* {id}\n"
        LLVMGenerator.reg += 1
        LLVMGenerator.buffer += f"%{LLVMGenerator.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %{LLVMGenerator.reg-1})\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def scanf_i32(id):
        LLVMGenerator.buffer += f"%{LLVMGenerator.reg} = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strsi, i32 0, i32 0), i32* {id})\n"
        LLVMGenerator.reg += 1
    
    @staticmethod
    def scanf_double(id):
        LLVMGenerator.buffer += f"%{LLVMGenerator.reg} = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strsd, i32 0, i32 0), double* {id})\n"
        LLVMGenerator.reg += 1



    @staticmethod
    def declare_i32(id,global_):
        if global_:
            LLVMGenerator.header_text += f"@{id} = global i32 0\n"
        else:
            LLVMGenerator.buffer += f"%{id} = alloca i32\n"
    
    @staticmethod
    def declare_double(id,global_):
        if global_:
            LLVMGenerator.header_text += f"@{id} = global double 0.0\n"
        else:
            LLVMGenerator.buffer += f"%{id} = alloca double\n"
    
    @staticmethod   
    def call(id):
        LLVMGenerator.buffer += f"%{LLVMGenerator.reg} = call i32 @{id}()\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def assign_i32(id, value):
        LLVMGenerator.buffer += f"store i32 {value}, i32* {id}\n"
    
    @staticmethod
    def assign_double(id, value):
        LLVMGenerator.buffer += f"store double {value}, double* {id}\n"
       
    @staticmethod
    def load_i32(id):
        LLVMGenerator.buffer += f"%{LLVMGenerator.reg} = load i32, i32* {id}\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def load_double(id):
        LLVMGenerator.buffer += f"%{LLVMGenerator.reg} = load double, double* {id}\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def add_i32(val1, val2):
        LLVMGenerator.buffer += f"%{LLVMGenerator.reg} = add i32 {val1}, {val2}\n"
        LLVMGenerator.reg += 1
    
    @staticmethod
    def add_double(val1, val2):
        LLVMGenerator.buffer += f"%{LLVMGenerator.reg} = fadd double {val1}, {val2}\n"
        LLVMGenerator.reg += 1
    
    @staticmethod
    def sub_i32(val1, val2):
        LLVMGenerator.buffer += f"%{LLVMGenerator.reg} = sub i32 {val2}, {val1}\n"
        LLVMGenerator.reg += 1
    
    @staticmethod
    def sub_double(val1, val2):
        LLVMGenerator.buffer += f"%{LLVMGenerator.reg} = fsub double {val2}, {val1}\n"
        LLVMGenerator.reg += 1
    
    @staticmethod
    def div_i32(val1, val2):
        LLVMGenerator.buffer += f"%{LLVMGenerator.reg} = sdiv i32 {val2}, {val1}\n"
        LLVMGenerator.reg += 1
    
    @staticmethod
    def div_double(val1, val2):
        LLVMGenerator.buffer += f"%{LLVMGenerator.reg} = fdiv double {val2}, {val1}\n"
        LLVMGenerator.reg += 1
    
    @staticmethod
    def mul_i32(val1, val2):
        LLVMGenerator.buffer += f"%{LLVMGenerator.reg} = mul i32 {val1}, {val2}\n"
        LLVMGenerator.reg += 1
    
    @staticmethod
    def mul_double(val1, val2):
        LLVMGenerator.buffer += f"%{LLVMGenerator.reg} = fmul double {val1}, {val2}\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def close_main():
        LLVMGenerator.main_text += LLVMGenerator.buffer
    

    @staticmethod
    def generate():
        text = "";
        text += "declare i32 @printf(i8*, ...)\n"
        text += "declare i32 @scanf(i8*, ...)\n"
        text += "@strpi = constant [4 x i8] c\"%d\\0A\\00\"\n"
        text += "@strpd = constant [4 x i8] c\"%f\\0A\\00\"\n"
        text += "@strps = constant [4 x i8] c\"%s\\0A\\00\"\n"
        text += "@strsi = constant [3 x i8] c\"%d\\00\"\n"
        text += "@strsd = constant [4 x i8] c\"%lf\\00\"\n"
        text += "\n"
        text += LLVMGenerator.header_text
        text += "define i32 @main() nounwind {\n"
        text += LLVMGenerator.main_text
        text += "  ret i32 0\n"
        text += "}\n"
        return text