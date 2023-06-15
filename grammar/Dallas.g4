grammar Dallas;

// Reguły startowe
prog : (statement SEMI)+ EOF;

block: LCURLY (statement SEMI)* RCURLY;

// Instrukcje
statement
    : variableDeclaration
    | assignment
    | printCall
    | readCall
    | ifElseStatement
    | ifStatement
    | functionDefinition
    | functionCall 
    | functionCallOnObject 
    | functionCallOnString
    | loopTill
    ;

variableDeclaration : dataType ID ;

assignment : ID ASSIGN expression;

// Wywołanie funkcji
printCall : PRINT LPAREN ID RPAREN ;

readCall : READ LPAREN ID RPAREN ;

functionCall : ID LPAREN (expression (COMMA expression)*)? RPAREN ;

functionCallOnObject : ID DOT functionCall ;

functionCallOnString : STRING DOT functionCall ;

array : LBRACK (expression (COMMA expression)*)? RBRACK ;

toInt: LPAREN INT_KEY RPAREN;

toFloat: LPAREN FLOAT_KEY RPAREN;

// Wyrażenia
expression
    : ID
    | functionCall
    | value
    | array
    | logicalExpression
    | additiveExpression        
    ;

logicalExpression
    : simpleLogicalExpression OR simpleLogicalExpression  #or
    | simpleLogicalExpression XOR simpleLogicalExpression #xor
    | simpleLogicalExpression AND simpleLogicalExpression #and
    | simpleLogicalExpression EQ simpleLogicalExpression  #equal
    | EXCLAMATION simpleLogicalExpression    #negation
    | BOOL                        #bool
    ;

simpleLogicalExpression
    : ID
    | INT
    | FLOAT
    | STRING
    | BOOL
    | additiveExpression
    ;

additiveExpression
    : multiplicativeExpression #singleValue3
    | additiveExpression PLUS multiplicativeExpression  #add
    | additiveExpression MINUS multiplicativeExpression #substract
    ;

multiplicativeExpression
    : unaryExpression #singleValue2
    | multiplicativeExpression ASTERISK unaryExpression #multiply
    | multiplicativeExpression SLASH unaryExpression    #divide
    ;

unaryExpression
    : primaryExpression #singleValue1
    | PLUS unaryExpression  #positive
    | MINUS unaryExpression #negative
    ;

primaryExpression
    : value                     #singleValue
    | LPAREN expression RPAREN  #paren
    | toInt expression          #toint
    | toFloat expression        #tofloat
    ;

// ifStatement: IF condition THEN ifBlock (ELSE condition THEN ifBlock)? ENDIF;
ifElseStatement: IF condition ifBlock ELSE elseBlock;
ifStatement: IF condition ifBlock;
condition :  LPAREN comparisonExp RPAREN;
comparisonExp
    : value LT value    #lesserThan
    | value LTE value   #lesserThanEqual
    | value GT value    #greaterThan
    | value GTE value   #greaterThanEqual
    | value EQ value    #isEqual
    | value NEQ value   #notEqual
    ;

ifBlock : block;
elseBlock : block;

//function
functionDefinition: dataType FUNCTION ID LPAREN (variableDeclaration (COMMA variableDeclaration)*)? RPAREN functionBlock;

//loop
loopTill: LOOP loopBlock TILL loopCondition;
loopBlock: block;
loopCondition: condition;

value
    : ID
    | INT
    | FLOAT
    | STRING
    | BOOL
    ;

dataType : INT_KEY
    | FLOAT_KEY
    | FLOAT_32_KEY
    | FLOAT_64_KEY
    | STRING_KEY
    | ARRAY_KEY
    | BOOL_KEY
    ;

PRINT:	'print' ;
READ:	'read' ;

IF: 'if';
THEN: 'then';
ELSE: 'else';
ENDIF: 'eif';

FUNCTION: 'function';
functionBlock: block;
// RETURN: 'return';
// returnStat: RETURN expression SEMI;

LOOP: 'loop';
TILL: 'till';

AND : '&&' ;
OR : '||' ;
XOR : '^^' ;
EQ : '==' ;
NEQ : '!=' ;
GT: '>';
GTE: '>=';
LT: '<';
LTE: '<=';
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
BOOL_KEY: 'bool' ;
ARRAY_KEY: 'array';

FLOAT : INT DOT INT ;
INT : [0-9]+ ;
STRING: DQ ~["\r\n]* DQ;
BOOL: TRUE | FALSE ;
TRUE: 'true';
FALSE:'false';

PLUS: '+' ;
MINUS: '-' ;
ASTERISK: '*' ;
SLASH: '/';
DOT: '.';
EXCLAMATION: '!';
DQ: '"';
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
WS: [ \t\n\r\f]+ -> skip ;
