%{
#include <stdio.h>
%}

%%
[0-9]+          { printf("Number: %s\n", yytext); }
[+-/*]          { printf("Operator: %s\n", yytext); }
[\n]            { printf("Newline\n"); }
[ \t]           ; // Ignore whitespace
.               { printf("Invalid character: %s\n", yytext); }
%%

int main() {
    yylex();
    return 0;
}


Save this file and then compile it using Flex to generate the C code:
flex lexer.l
gcc lex.yy.c -o lexer -lfl

Now, you can run the generated lexer executable and input arithmetic expressions to
see how the lexical analyzer tokenizes them:
./lexer