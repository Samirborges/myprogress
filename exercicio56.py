name = 0
maidade = 0
midade = 0
idademulheres = 0
qmulheres = 0

for grup in range (0, 4):
    print('Dados da {}° pessoa:'.format(grup + 1))
    nome = str(input('\033[mDigite seu nome:\033[33m '))
    idade = int(input('\033[mDigite a sua idade:\033[33m '))
    sexo = str(input('\033[mDigite o seu sexo:\033[33m ')).lower().strip()
    print('\033[m='*30)
    midade += idade #Calculadora da méida das idades
    
    if grup == 0 and sexo == 'masculino': #calculadora da idade do homem mais velho
        maidade = idade
        name = nome
    elif grup != 0 and sexo == 'masculino':
        if idade > maidade:
            maidade = idade
            name = nome
    
    if sexo == 'feminino' and idade < 20:
        qmulheres += 1

print('='*30)
print(f'\033[mMédia da idade\033[34m {midade/4}\033[m')
print(f'Nome do homem mais velho tem \033[33m{maidade} \033[31m{name}\033[m')
print(f'Quantidade de mulheres com menos de 20 anos:\033[32m {qmulheres}\033[m')    
print('{:=^40}'.format(' O programa acabou '))