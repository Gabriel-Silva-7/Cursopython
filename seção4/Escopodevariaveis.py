'''
Dois casos de escopo

1 - Variaveis golbais;
 -variaveis globais sao reconhecidas ou seja seu escopo compreende todo o progama

 2- variaveis locais
 -variaveis locais sao reconhecidas apenas no bloco onde foram declaradas ou seja seu escopo esta limitado ao bloco onde foi declarada.


para declarara variaveis fazemos

nome_da_variavel = valor_da_variavel


python é uma linguagem de tipagem dinamica isso significa que ao clararmos uma variavel nos nao colocamos o tipo de dados dela 

exemplo em c
int numero = 42;

exempo em java
int numero = 42;



'''

numero = 42
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

nao_existo = 'oi'
print(nao_existo)


numero = 42

if numero > 10:
    novo = numero + 10 # a variavel 'novo' esta declarada dentro do bloco do if sendo assim é uma variavel local
    print(novo)

print(novo)