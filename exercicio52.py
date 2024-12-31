tot = 0
num = int(input('Digite um número: '))
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} \033[m'.format(c), end='')
if tot == 2:
    print(f'\nO número foi divisível {tot} vezes, ele é primo.')
else:
    print(f'\nO número foi divisível {tot} vezes, não é primo.')
