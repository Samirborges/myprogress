num = int(input('Digite um número inteiro qualquer: '))
print('''Escolha qual tipo você quer converter:
[1] Binário
[2] Octal
[3] Hexadecimal''')
esc = int(input('Sua opção: '))
if esc == 1:
    print('O número que você escolheu em binário é: {}'.format(bin(num)[2:]))

elif esc == 2:
    print('O número que você escolheu em octal fica: {}'.format(oct(num)[2:]))
    
elif esc == 3:
    print('O número que você escolheu em hexadecimal fica: {}'.format(hex(num)[2:]))