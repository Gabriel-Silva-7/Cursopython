m = "manha"
n = "noite" 
t = "tarde"


turno = input('qual o seu turno? (m=manha), (t=tarde), (n=noite) ')

if (turno == 'n') :
    print(f'voce selecionou o turno da {n}, Boa noite')
elif (turno == 'm') :
    print(f'voce selecionou o turno da {m}, bom dia')
elif (turno == 't'):
    print(f'voce selecionou o turno da {t},boa tarde')
else :
    print('entrada invalida')