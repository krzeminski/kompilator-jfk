grammar Dallas;

// Reguły startowe
start : statement+ EOF;

// Instrukcje
statement : variableDeclaration
          | functionCall
          | assignment
          ;

// Deklaracja zmiennych
variableDeclaration : dataType ID SEMI ;

// Wywołanie funkcji
functionCall : ID LPAREN (expression (COMMA expression)*)? RPAREN ;

functionCallOnObject : ID DOT functionCall ;

// Przypisanie wartości
assignment : ID ASSIGN expression SEMI ;

// Wyrażenia
expression: ID
    | INT
    | FLOAT
    | STRING
    | assignment
    | functionCall
    | expression
    | logicalExpr
    | mathExpr
    ;

logicalExpr : logicalOrExpr
    | logicalXorExpr
    | logicalAndExpr
    | negationExpr
    | equalityExpr
    ;

logicalOrExpr : expression (OR expression)* ;

logicalXorExpr : expression (XOR expression)* ;

logicalAndExpr : expression (AND expression)* ;

negationExpr : EXCLAMATION expression ;

equalityExpr : expression ( EQ expression)* ;

mathExpr : NUMBER (MATH_OPERATOR NUMBER)*
    | additionExpr
    | substractionExpr
    | multiplicationExpr
    | divisionExpr
    ;

additionExpr : mathExpr (PLUS mathExpr)* ;

substractionExpr : mathExpr (MINUS mathExpr)* ;

multiplicationExpr : mathExpr (ASTERISK mathExpr)* ;

divisionExpr : mathExpr (SLASH mathExpr)* ;

dataType : INT_KEY
    | FLOAT_KEY
    | FLOAT_32_KEY
    | FLOAT_64_KEY
    | STRING_KEY
    ;

mathOperator: PLUS | MINUS | ASTERISK | SLASH;

AND : '&&' ;
OR : '||' ;
XOR : '^^' ;
EQ : '==' ;
ASSIGN : '=';
COMMA : ',' ;
SEMI : ';' ;
LPAREN : '(' ;
RPAREN : ')' ;
LCURLY : '{' ;
RCURLY : '}' ;
    
INT_KEY: 'int' ;
FLOAT_KEY: 'float'
FLOAT_32_KEY: 'float32'
FLOAT_64_KEY: 'float64'
STRING_KEY: 'string' ;

INT : [0-9]+ ;
STRING: ".*?" ;
FLOAT : INT DOT INT ;

NUMBER : ( PLUS | MINUS )? (INT | FLOAT) ;
PLUS: + ;
MINUS: - ;
ASTERISK: * ;
SLASH: / ;
DOT: . ;
EXCLAMATION: '!';

ID: [a-zA-Z_][a-zA-Z_0-9]* ;
WS: [ \t\n\r\f]+ -> skip ;
