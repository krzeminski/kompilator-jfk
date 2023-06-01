grammar Dallas;

// Reguły startowe
start : statement+ EOF;

// Instrukcje
statement : variableDeclaration
          | functionCall SEMI
          | assignment 
          | expression SEMI
          ;

// Deklaracja zmiennych
variableDeclaration : dataType ID SEMI ;

// Wywołanie funkcji
functionCall : ID LPAREN (expression (COMMA expression)*)? RPAREN ;

functionCallOnObject : ID DOT functionCall ;

// Przypisanie wartości
assignment : ID ASSIGN expression SEMI ;

// Wyrażenia
expression : ID
    | INT
    | FLOAT
    | STRING
    | assignment
    | functionCall
    | expression OR expression
    | expression XOR expression 
    | expression AND expression 
    | expression EQ expression 
    | EXCLAMATION expression 
    | mathExpr
    | mathExpr (PLUS mathExpr)* 
    | mathExpr (MINUS mathExpr)* 
    | mathExpr (ASTERISK mathExpr)* 
    | mathExpr (SLASH mathExpr)* 
    ;

mathExpr : NUMBER (mathOperator NUMBER)* ;

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
FLOAT_KEY: 'float';
FLOAT_32_KEY: 'float32';
FLOAT_64_KEY: 'float64';
STRING_KEY: 'string' ;

INT : [0-9]+ ;
STRING: DQ ~["\r\n]* DQ;
FLOAT : INT DOT INT ;

NUMBER : ( PLUS | MINUS )? (INT | FLOAT) ;
PLUS: '+' ;
MINUS: '-' ;
ASTERISK: '*' ;
SLASH: '/';
DOT: '.';
EXCLAMATION: '!';
DQ: '"';
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
WS: [ \t\n\r\f]+ -> skip ;
