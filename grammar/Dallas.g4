grammar Dallas;

// Reguły startowe
prog : (statement SEMI)+ EOF;

// Instrukcje
statement
    : variableDeclaration
    | assignment
    | printCall 
    | readCall 
    | functionCall 
    | functionCallOnObject 
    | functionCallOnString 
    ;

variableDeclaration : dataType ID ;

assignment : ID ASSIGN expression;

// Wywołanie funkcji
printCall : PRINT LPAREN expression RPAREN ;

readCall : READ LPAREN expression RPAREN ;

functionCall : ID LPAREN (expression (COMMA expression)*)? RPAREN ;

functionCallOnObject : ID DOT functionCall ;

functionCallOnString : STRING DOT functionCall ;

array : LBRACK (expression (COMMA expression)*)? RBRACK ;

// Wyrażenia
expression
    : ID
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
    : value
    | LPAREN expression RPAREN
    | TOINT expression 
    | TOFLOAT expression 
    ;

value
    : ID
    | INT
    | FLOAT
    | STRING
    ;

dataType : INT_KEY
    | FLOAT_KEY
    | FLOAT_32_KEY
    | FLOAT_64_KEY
    | STRING_KEY
    | ARRAY_KEY
    ;

PRINT:	'print' ;
READ:	'read' ;
TOINT: LPAREN INT_KEY RPAREN ;
TOFLOAT: LPAREN FLOAT_KEY RPAREN ;

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
ARRAY_KEY: 'array';

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
