value = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')),)
print(f'Você digitou os valores: {value}')
valuestr = str(value)
print(f'O valor 9 apareceu {valuestr.count('9')} vezes') # Na parte de contar o nove não precisava transformar em string.
if valuestr.count('3') < 1:
    print('O valor 3 não foi digitado.')
else:
    print(f'O valor 3 foi digitado na {value.index(3)+1}° posição.')
print('Os valores pares digitados foram ', end='')
for c in range(0, 4):
    if value[c] % 2 == 0:
        print(f'{value[c]} ', end='')
