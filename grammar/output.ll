declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)
@strpi = constant [4 x i8] c"%d\0A\00"
@strpd = constant [4 x i8] c"%f\0A\00"
@strps = constant [4 x i8] c"%s\0A\00"
@strsi = constant [3 x i8] c"%d\00"
@strsd = constant [4 x i8] c"%lf\00"

@a = global double 0.0
@b = global i32 0
@x = global i32 0
@y = global double 0.0
define i32 @main() nounwind {
%1 = fmul double 3.1, 2.5
store double %1, double* @a
%2 = load double, double* @a
%3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %2)
%4 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strsi, i32 0, i32 0), i32* @b)
%5 = load i32, i32* @b
%6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %5)
%7 = mul i32 8, 5
store i32 %7, i32* @x
%8 = load i32, i32* @x
%9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %8)
%10 = fadd double 3.9, 5.1
%11 = fmul double 5.0, %10
%12 = fadd double 4.0, %11
store double %12, double* @y
%13 = load double, double* @y
%14 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %13)
  ret i32 0
}
