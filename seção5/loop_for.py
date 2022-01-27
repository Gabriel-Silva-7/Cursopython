"""
loop fore
for item in interavel:
    //execução do loop

Os loops são ultilizados para interar sequencias ou sobre valores iteraveis


Exemplo de itaraveis
 -String
  nome= Bielss
- Lista
    Lista = [1, 3, 5, 7, 9]
-Range 
    numeros = Range(1, 10)

"""
#exemplo de For 1
import enum


nome = 'Bielss'
Numeros = range(1, 3) # temos que transformar em uma lista
Lista = [1, 3, 5, 7, 9]

for letra in nome:
    print(letra)

#exemplo 2

for numero in Lista:
    print(numero)

#exemplo 3

for numero in range(1,10):
    print(numero)
#valor final de um range não é incluido
'''
for indice, v in enumerate(nome):
    print(nome[indice])
   
    Enumerate
    (0, 'B), (1, I), (2, E), (3, L)


    for _, letra in enumerate(nome):
    print(letra)

    Quando nao precisamos de um valor podemos descartar tal valor ultilizando _
    '''

for valor in enumerate(nome):
    print(valor)



qtd= int(input('quantas vezes esse loop deve rodar? '))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}' )