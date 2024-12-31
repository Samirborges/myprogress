from random import randint
from time import sleep
mega = list()
game = int(input('Quantos jogos você quer eu eu sortei? '))
print('{:=^30}'.format(f' SORTEANDO {game} JOGOS '))

for c in range(0, game):
    while len(mega) != 6:
        number = randint(1, 60)
        if number not in mega:
               mega.append(number)
    print(f'Jogo {c+1}: {sorted(mega)}')
    sleep(1)
    mega.clear()

print('{:=^30}'.format(' < BOA SORTE! > '))
