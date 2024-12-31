option = ''
numberlist = list()
while option != 'n':
    numberlist.append(int(input('Digite um valor: ')))
    option = str(input('Quer continuar? [S/N] ')).lower()

print(f'Você digitou {len(numberlist)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(numberlist)[::-1]}')
# Nesse print como eles querem apareçer de forma degrecente, pode se ter utilizado numberlist.sorted(reverse=True)

if 5 in numberlist:
    print('O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 não faz parte da lista!')
    