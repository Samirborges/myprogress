fat = int(input('Digite um número qualquer: '))
fot = fat
cont = 1
print('O fatorial de \033[36m{}!\033[m '.format(fat), end='')
while fot != 0:
    print(f'{fot}', end='')
    print(' x ' if fot > 1 else ' = ', end='')
    cont *= fot
    fot = (fot - 1)
print(f'\033[1;35m{cont}\033[m')
print('FIM DO PROGRAMA')