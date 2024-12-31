print('Gerador de PA')
print('{:=^10}'.format('='))
number = int(input('Digite o primeiro termo: '))
progress = int(input('Digite a PA: '))
cont = 1
while cont <= 10:
    print('{} → '.format(number), end='')
    number += progress
    cont += 1
print('FIM')