import math
'''
#exercicio 1
numero1 = float(input("digite o primeiro numero"))
numero2 = float(input("digite o segundo numero"))

if numero1>numero2 :
    {print(f'o maior numero é o numero {numero1}')}
else:
    {print(f'o maior numero é o numero {numero2}')}


#exercicio 2
numero3 = float(input(f'\ndigite um numero\n'))



if numero3 >= 0 :
    raiz = math.sqrt(numero3)
    print(f'\nA raiz quadrada de {numero3} é {raiz}\n')
else :
    print(f'\nNumero invalido')
'''
'''
#exercicio 3
numero4 = float(input(f'\ndigite um numero\n'))
if numero4 >= 0 :
    raiz = math.sqrt(numero4)
    print(f'\nA raiz quadrada de {numero4} é {raiz}\n')
else :
    aoquadrado = (numero4*numero4)
    print(f'\nO numero ao quadrado é {aoquadrado}')
'''
'''
#exercicio 4
numero5 = float(input(f'\ndigite um numero\n'))
if numero5 > 0:
    print(f'o numero ao quadrado é {numero5*numero5}')
    raiz = math.sqrt(numero5)
    print(f'\nA raiz quadrada de {numero5} é {raiz}\n')
'''
'''
#exercicio 5
numero6 = int(input(f'\nescreva um numero \n'))
resultado = (numero6%2)
print(resultado)
if resultado == 0:
    print('numero par')
else:
    print('numero impar')
'''
'''
#exercicio 6 e 7
numero7 = int(input(f'\nescreva um numero \n'))
numero8 = int(input(f'\nescreva um numero \n'))

if numero8>numero7 :
    print(f'o maior numero é o {numero8}')
    print(f'A diferença entre os numero é = {numero8-numero7}')
elif numero7 == numero8:
    print(f'Os numeros são iguais')
else :
    print(f'o maior numero é o {numero7}')
    print(f'A diferença entre os numero é = {numero7-numero8}')
'''


'''
#exercicio 8
nota1 = float(input('\nDigite a primeira nota\n'))
nota2 = float(input('\nDigite a segunda nota\n'))
if nota1 in range(0,10) and nota2 in range(0,10):
    print((nota1+nota2)/2)
else:
    print('nota invalida')
'''


#exercicio 9
salario = int(input('\ninsira seu salario\n'))
valortotalemprestimo = int(input('\n insira o valor do emprestimo \n'))
numerodeparcelasdoemprestimo = int(input('\ninsira o numero de parcelas do emprestimo\n'))
valordaparcela = (valortotalemprestimo/numerodeparcelasdoemprestimo)
print(f'o valor da parcela ficara \n{valordaparcela}')
vintePorCentoDoSalario = ((salario/100)*20)

if valordaparcela>vintePorCentoDoSalario:
    print('desculpe no momento não temos uma oferta para voce')
else:
    print('emprestimo concedido')