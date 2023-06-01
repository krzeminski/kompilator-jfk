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

logicalOrExpr : logicalAndExpr ('||' logicalAndExpr)* ;

logicalAndExpr : equalityExpr ('&&' equalityExpr)* ;

equalityExpr : comparisonExpr (('=' | '!=' | '==' | '^^') comparisonExpr)* ;

comparisonExpr : additiveExpr (('>' | '>=' | '<' | '<=') additiveExpr)* ;

additiveExpr : multiplicativeExpr (('+' | '-') multiplicativeExpr)* ;

multiplicativeExpr : unaryExpr (('*' | '/') unaryExpr)* ;

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

WS : [ \t\r\n]+ -> skip ;  // Ignoruj białe znaki
