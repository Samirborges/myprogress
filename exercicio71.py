print('\033[1m-\033[m'*40)
print('BANCO CEV')
print('\033[1m-\033[m'*40)
value = int(input('Qual valor você que sacar?: \033[1;32mR$'))
config = 0
if value > 50: #Calculadora de cédulas
    config = value % 50
    receb50 = int(value/50)
    print(f'\033[mTotal de \033[1;35m{receb50}\033[m cédulas de \033[1;32mR$50\033[m')
if value > 20 and config > 1: 
    receb20 = int(config/20)
    value = config % 20
    print(f'\033[mTotal de \033[1;35m{receb20}\033[m cédulas de \033[1;32mR$20\033[m')
if value > 10 and config > 1:
    receb10 = int(value/10)
    config = value % 10
    print(f'\033[mTotal de \033[1;35m{receb10}\033[m cédulas de \033[1;32mR$10\033[m')
if value > 1 and config > 1:
    receb1 = int(config/1)
    print(f'\033[mTotal de \033[1;35m{receb1}\033[m cédulas de \033[1;32mR$1\033[m')
print('='*40)
print('Volte sempre ao Banco CEV! Tenha um bom dia!')
