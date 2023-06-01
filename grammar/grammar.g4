grammar MyLanguage;

// Reguły startowe
start : statement+ EOF;

// Instrukcje
statement : variableDeclaration
          | functionCall
          | assignment
          ;

// Deklaracja zmiennych
variableDeclaration : dataType ID ';' ;

// Wywołanie funkcji
functionCall : ID '(' (expression (',' expression)*)? ')' ';' ;

// Przypisanie wartości
assignment : ID '=' expression ';' ;

// Wyrażenia
expression : logicalOrExpr ;

logicalOrExpr : expression ('||' expression)* ;

logicalAndExpr : expression ('&&' expression)* ;

equalityExpr : expression ( '==' expression)* ;

comparisonExpr : expression (('>' | '>=' | '<' | '<=') expression)* ;

mathExpr : NUMBER (MATH_OPERATOR NUMBER)*;

additionExpr : mathExpr (PLUS mathExpr)* ;

substractionExpr : mathExpr (('+' | '-') mathExpr)* ;

multiplicationExpr : mathExpr (('*' | '/') mathExpr)* ;

divisionExpr : mathExpr (('*' | '/') mathExpr)* ;

unaryExpr : ('!' | '-')? primaryExpr ;

primaryExpr : ID
            | NUMBER
            | '(' expression ')'
            | arrayOperations
            | stringOperations
            ;

// Operacje na tablicach
arrayOperations : ID ('.push' | '.pop' | '.get' | '.length') ;

// Operacje na ciągach znaków
stringOperations : ID ('.concat' | '.length' | '.toUpper' | '.toLower') ;

// Typy danych
dataType : 'int' | 'float' | 'float32' | 'float64' ;

// Tokeny
ID : [a-zA-Z]+ ;
NUMBER : ('+' | '-')? DIGIT+ ('.' DIGIT+)? ;
fragment DIGIT : [0-9] ;
PLUS: + ;
MATH_OPERATOR: PLUS | MINUS | ASTERISK | SLASH;

WS : [ \t\r\n]+ -> skip ;  // Ignoruj białe znaki
