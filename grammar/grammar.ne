@{%
const moo = require('moo');

const lexer = moo.compile({
    white_space: {match: / /, lineBreaks: true},
    indent: '\t',
    comment: {match: /\/\/.*?$/, lineBreaks: true, error: true},
    newline: {match: /\r\n|[\r\n]/, lineBreaks: true},
    number: /[0-9]+/,
    string: /".*?"/,
    left_parenthesis: '(',
    right_parenthesis: ')',
    comma: ',',
    colon: ':',
    semicolon: ';',
    hash: '#',
    class: '.',
    universal_selector: '*',
    function_call: /[a-zA-Z_\-]*\(.*\)/,
    combinator: /[+>~ ]/,
    percentage: /%/,
    unit: /'px' | 'em' | 'rem' | 'vh' | 'vw' | 'vmin' | 'vmax' | 'cm' | 'mm' | 'in' | 'pt' | 'pc'/,
    important: /important/,
    identifier: /[0-9a-zA-Z_][a-zA-Z0-9_\-]*/,
    exclamation_mark: /\!/
});
%}

@lexer lexer

stylesheet -> (ruleset | ignore):* {% id %}

ruleset -> selectors declarations %newline {% id %}

selectors -> selector ("," newline selector):* newline {% id %}

selector -> simple_selector_sequence (combinator simple_selector_sequence):* {% id %}

simple_selector_sequence -> negation:? hash:? class:? type_selector:? universal_selector:? pseudo_class:? attribute:? {% id %}

type_selector -> element_name {% id %}

universal_selector -> "*" {% id %}

class -> "." classname {% id %}

pseudo_class -> ":" pseudo_class_name {% id %}

negation -> ":not(" simple_selector_sequence ")" {% id %}

attribute -> "[" attribute_name "]" {% id %}

combinator -> "+" | ">" | "~" | " " {% id %}

declarations -> declaration (semicolon newline declaration):* newline{% id %}

indent -> %indent

declaration -> indent property ":" white_space values important:? semicolon:? comment:? {% id %}

property -> %identifier {% id %}

values -> value ( white_space value):* {% id %}

value -> %identifier | %string | url |  color | length | number | percentage {% id %}

important -> white_space:? exclamation_mark "important" {% id %}

url -> %function_call {% id %}

color -> hex_color {% id %}

hex_color -> hash %identifier | hash number {% id %}

length -> number ("px" | "em" | "rem" | "vh" | "vw" | "vmin" | "vmax" | "cm" | "mm" | "in" | "pt" | "pc") {% id %}

number -> digits {% id %}

percentage -> number "%" {% id %}

digits -> [0-9]:+ {% id %}

identifier -> %identifier {% id %}

string -> %string {% id %}

element_name -> %identifier {% id %}

id -> hash %identifier {% id %}

hash -> "#" {% id %}

exclamation_mark -> %exclamation_mark {% id %}

classname -> %identifier {% id %}

pseudo_class_name -> %identifier {% id %}

attribute_name -> %identifier {% id %}

white_space -> %white_space {% id %}

newline -> %newline | comment %newline {% id %}

semicolon -> %semicolon {% id %}

comment -> white_space:? %comment {% id %}

ignore -> comment %newline {% id %}