# LogicaDaComputacao-APS
Atividade Pratica Supervisionada para a disciplina de Lógica da Computação - Linguagem de programação

```
BLOCK = "{", { COMMAND }, "}" ; 
COMMAND = ( λ | ASSIGNMENT | PRINT | BLOCK | WHILE | IF), ";" ; 
WHILE = "inquantu", "(", OREXPR ,")", COMMAND;
IF = "si", "(", OREXPR ,")", COMMAND, (("sinaum", COMMAND) | λ );
ASSIGNMENT = IDENTIFIER, "=", EXPRESSION ; 
PRINT = "printy", "(", OREXPR, ")" ; 
OREXPR = ANDEXPR, { "ow", ANDEXPR } ;
ANDEXPR = EQEXPR, { "i", EQEXPR } ;
EQEXPR = RELEXPR, { "==", RELEXPR } ;
RELEXPR = EXPRESSION, { (">"|"<"),  EXPRESSION }
EXPRESSION = TERM, { ("+" | "-"), TERM } ; 
TERM = FACTOR, { ("*" | "/"), FACTOR } ; 
FACTOR = (("+" | "-" | "!" ), FACTOR) | NUMBER | "(", OREXPR,  ")" | IDENTIFIER | READLN;
READLN = "imputi", "(",")";
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ; 
NUMBER = DIGIT, { DIGIT } ; 
LETTER = ( a | ... | z | A | ... | Z ) ; 
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
```