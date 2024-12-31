from time import sleep
from random import randint
print('\033[1;33mJokenpô \033[m')
computador = int(randint(1, 3))
jogador = str(input('Opção: '))
print('JO', end='')
sleep(1)
print('KEN', end='')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*30)
if jogador == 'pedra' and computador == 3 or jogador == 'papel' and computador == 1 or jogador == 'tesoura' and computador == 2:
    print('\033[1;32mVocê venceu!\033[m')

elif jogador == 'pedra' and computador == 1 or jogador == 'papel' and computador == 2 or jogador == 'tesoura' and computador == 3:
    print('\033[1;33mEMPATE!\033[m')
    
else:
    print('\033[1;31mVocê perdeu!\033[m')

if computador == 1:
    computador = 'pedra'
elif computador == 2:
    computador = 'papel'
else:
     computador = 'tesoura'
print('O computador jogou: {}'.format(computador))
print('-='*30)
