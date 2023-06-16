declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)
@strpi = constant [4 x i8] c"%d\0A\00"
@strpd = constant [4 x i8] c"%f\0A\00"
@strps = constant [4 x i8] c"%s\0A\00"
@strsi = constant [3 x i8] c"%d\00"
@strsd = constant [4 x i8] c"%lf\00"

define i32 @main() nounwind {
%9 = sitofp i32 1 to double
%1 = fmul double 3.1, 2.5
store double %1, double* @a
store i32 2, i32* @b
%2 = alloca i32
store i32 0, i32* %2
br label %cond1
cond1:
%3 = load i32, i32* %2
%4 = add i32 %3, 1
store i32 %4, i32* %2
%5 = icmp slt i32 %3, 5
br i1 %5, label %true1, label %false1
true1:
%6 = load double, double* @a
%7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %6)
%8 = load double, double* @a
%10 = fsub double a, %9
store double %10, double* @a
br label %cond1
false1:
  ret i32 0
}
