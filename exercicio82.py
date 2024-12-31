numberlist = list()
option = ''
while option != 'n':
    numberlist.append(int(input('Digite um número: ')))
    option = str(input('Você quer continuar? [S/N] ')).lower()
print(f'A lista completa é {numberlist}')
numberlistpar = list()
numberlistimpar = list()
for c in range(len(numberlist)):
    if numberlist[c] % 2 == 0:
        numberlistpar.append(numberlist[c])
    else:
        numberlistimpar.append(numberlist[c])
print(f'A lista de pares é {numberlistpar}')
print(f'A lista de ímpares é {numberlistimpar}')
