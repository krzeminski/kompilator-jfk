declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)
@strpi = constant [4 x i8] c"%d\0A\00"
@strpd = constant [4 x i8] c"%f\0A\00"
@strps = constant [4 x i8] c"%s\0A\00"
@strsi = constant [3 x i8] c"%d\00"
@strsd = constant [4 x i8] c"%lf\00"

define i32 @main() nounwind {
%d = alloca i32
store i32 0, i32* %%d
%e = alloca i32
store i32 5, i32* %%e
%1 = load i32, i32* %%d
%2 = load i32, i32* %%e
%3 = load i32, i32* %%
%4 = icmp eq i32 %3,VarType.INT
%5 = load i32, i32* %%e
%6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %5)
  ret i32 0
}
