grammar Dallas;

// Reguły startowe
start : statement+ EOF;

// Instrukcje
statement : variableDeclaration
          | functionCall SEMI
          | functionCallOnObject SEMI
          | functionCallOnString SEMI
          | assignment
          | expression SEMI
          ;

// Deklaracja zmiennych
variableDeclaration : dataType ID SEMI ;

// Wywołanie funkcji
functionCall : ID LPAREN (expression (COMMA expression)*)? RPAREN ;

functionCallOnObject : ID DOT functionCall ;

functionCallOnString : STRING DOT functionCall ;

array : LBRACK (expression (COMMA expression)*)? RBRACK ;

// Przypisanie wartości
assignment : ID ASSIGN expression SEMI;

// Wyrażenia
expression : ID
    | assignment
    | functionCall
    | expression OR expression
    | expression XOR expression 
    | expression AND expression 
    | expression EQ expression 
    | EXCLAMATION expression 
    | additiveExpression
    | INT
    | FLOAT
    | STRING
    | array
    ;

additiveExpression
    : multiplicativeExpression
    | additiveExpression PLUS multiplicativeExpression
    | additiveExpression MINUS multiplicativeExpression
    ;

multiplicativeExpression
    : unaryExpression
    | multiplicativeExpression ASTERISK unaryExpression
    | multiplicativeExpression SLASH unaryExpression
    ;

unaryExpression
    : primaryExpression
    | PLUS unaryExpression
    | MINUS unaryExpression
    ;

primaryExpression
    : INT
    | FLOAT
    | LPAREN expression RPAREN
    | ID
    ;

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
LBRACK : '[' ;
RBRACK : ']' ;
    
INT_KEY: 'int' ;
FLOAT_KEY: 'float';
FLOAT_32_KEY: 'float32';
FLOAT_64_KEY: 'float64';
STRING_KEY: 'string' ;

FLOAT : INT DOT INT ;
INT : [0-9]+ ;
STRING: DQ ~["\r\n]* DQ;

PLUS: '+' ;
MINUS: '-' ;
ASTERISK: '*' ;
SLASH: '/';
DOT: '.';
EXCLAMATION: '!';
DQ: '"';
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
WS: [ \t\n\r\f]+ -> skip ;
