'''
estruturas logicas and, or, not, is

operadores unitarios
 -not, is
 operadores binarios
 -and, or

para o end ambos valores precisam ser true
para o or um ou outro podem ser verdadeiros
para o not p valor do booleano é invertido ou seja se foir true vira false se for False vira True
'''

ativo = True
logado = True

if ativo and logado:
    print('Bem vindo usuário!')
else:
    print('voce precisa ativar sua conta. Por favor cheque seu e-mail')

if ativo or logado:
    print('Bem vindo usuário!')
else:
    print('voce precisa ativar sua conta. Por favor cheque seu e-mail')

if not ativo:
    print('voce precisa ativar sua conta. Por favor cheque seu e-mail')
else:
    print('bem vindo usuario!')

print(not True)
print(not False)


if logado is True:
    print('baah')

print(ativo is True)

if ativo is True:
    print(ativo)
else:
    print(logado)

passwordlogin = "gg"

if ativo is True:
    password = input("input your password")
    if password == passwordlogin:
        print('login sucess')
    else:
        print("Incorrect password")
else:
    print("active your account")