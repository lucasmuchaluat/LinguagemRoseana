# Linguagem de programação Roseana
Repositório para entrega da APS de Lógica da Computação 2021.1

## Objetivo:
* Criar uma Linguagem de Programação
* A linguagem deve ter todas as estruturas básicas de uma linguagem de programação: variáveis, condicionais, loops e funções.

## A Linguagem
A ideia consistem em adaptar uma linguagem de programação qualquer para o contexto léxico de Guimarães Rosa, um dos nossos maiores expressionistas literários. Autor de [Grande Sertão Veredas](https://guiadoestudante.abril.com.br/estudo/grande-sertao-veredas-resumo-da-obra-de-guimaraes-rosa/), João Guimarães Rosa foi um dos maiores escritores da literatura brasileira e, certamente, um dos mais importantes autores da língua portuguesa, língua que soube como nenhum outro escritor, reinventar. Ele é conhecido por sua tamanha originalidade e habilidade de inventar palavras. Ele, inclusive, possui um dicionário que ajuda os leitores a entenderem sua escrita baseada em neologismos roseanos. Portanto, o projeto adaptará uma linguagem de programação para que amantes da literatura brasileira e do estilo Roseano criem gosto por "codar"!

## Neologismos:
* **return (retorno da função) =** Batoque – s.m. – Sinal na orelha de animais de criação. Uma identificação.
* **if statement =** Bispar¹ – v.t. – Bisbilhotar; olhar atentamente, prestar atenção.
* **else statement =** Borra(ô) – s.f. – Resto; sobra. Borra de café.
* **while statement =** Ramerrão – s.m. – Repetição monótona, enfadonha. “Florzinha já não era lembrada no corre-corre, no ramerrão, no disse-que-disse da cidade” (Lima, Anfrísio. Espinho de Mandacaru, 2009:136).
* **print =** Escancarar² – v.t. – Exibir; mostrar.
* **readln =** Candonga – s.f. – Ver cadonga.


## EBNF:
```
BLOCK = { "{", COMMAND, "}" } ;
COMMAND = ( λ | ASSIGNMENT | PRINT | WHILE | IF | FUNCTION | RETURN | READLN | TYPES ), ";" ;
TYPES = ("bool" | "int" | "string")
DECLARATION = TYPES, IDENTIFIER ;
ASSIGNMENT = IDENTIFIER, "=", EXPRESSION ;
PRINT = "escancarar", "(", EXPRESSION, ")" ;
READLN = "candonga", "(",")" ;
EXPRESSION = TERM, { ("+" | "-"), TERM } ;
TERM = FACTOR, { ("*" | "/"), FACTOR } ;
FACTOR = (("+" | "-"), FACTOR) | NUMBER | "(", EXPRESSION, ")" | IDENTIFIER ;
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
NUMBER = DIGIT, { DIGIT } ;
LETTER = ( a | ... | z | A | ... | Z ) ;
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
ARGUMENT = ARGUMENT, { (",", ARGUMENT) } ;
BOOL = ("true" | "false") ;
FUNCTION = TYPES, IDENTIFIER, "(", {ARGUMENT}, ")", BLOCK ;
RETURN = "batoque", { EXPRESSION } ;
LOGICAL-OPERATORS = ( "<" | ">" | "<=" | ">=" | "==" | "!=" | "&&" | "||" | "!" ) ;
CONDITION = (EXPRESSION, LOGICAL-OPERATORS, EXPRESSION) ;
IF = "bispar", "(", CONDITION, ")", BLOCK, {ELSE} ;
ELSE = "borra", (BLOCK | IF) ;
WHILE = "ramerrao", "(", CONDITION, ")", BLOCK ; 
```