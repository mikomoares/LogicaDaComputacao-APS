# LogicaDaComputacaoRoteiros
APS da matéria de Lógica da Computação - Criação de Linguagem de Programação


Para rodar um programa crie um arquivo, e utilize o comando a seguir:

`python compilador.py <arquivo>`

Exemplo (criando um arquivo "expressão1.c):

`python compilador.py expressão1.c`

Alguns exemplos de programa podem ser encontrados na pasta "Exemplos".

### Diagrama Sintático:

<img src=Diagrama+-.png>

### EBNF:

```
FUNCDEFBLOCK = (λ | TYPE,IDENTIFIER, "(", {TYPE, IDENTIFIER},{(",",TYPE,IDENTIFIER)}, ")", COMMAND);
BLOCK = "{", { COMMAND }, "}" ; 
COMMAND = ( λ | ASSIGNMENT | PRINTY | BLOCK | INQUANTU | SI | DECLARATOR | RET), ";" ; 
RET = "ret", OREXPRESSION
DECLARATOR = (INT | BOOL | STRING), IDENTIFIER;
INQUANTU = "INQUANTU", "(", OREXPR ,")", COMMAND;
SI = "si", "(", OREXPR ,")", COMMAND, (("sinaum", COMMAND) | λ );
ASSIGNMENT = IDENTIFIER, "=", EXPRESSION ; 
PRINTY = "printy", "(", OREXPR, ")" ; 
OREXPR = ANDEXPR, { "ow", ANDEXPR } ;
ANDEXPR = EQEXPR, { "ii", EQEXPR } ;
EQEXPR = RELEXPR, { "==", RELEXPR } ;
RELEXPR = EXPRESSION, { (">"|"<"),  EXPRESSION }
EXPRESSION = TERM, { ("+" | "-"), TERM } ; 
TERM = FACTOR, { ("*" | "/"), FACTOR } ; 
FACTOR = (("+" | "-" | "!" ), FACTOR) | NUMBER | STRING | BOOL | "(", OREXPR,  ")" | IDENTIFIER | IMPUTI;
READLN = "readln", "(",")";
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" }, { "(", {(OREXPR), ","}, ")" } ;
NUMBER = DIGIT, { DIGIT } ; 
STRING = '"', { LETTER | DIGIT }, '"' ; 
LETTER = ( a | ... | z | A | ... | Z ) ; 
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;

```
