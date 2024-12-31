from random import randint
print('{:=^40}'.format('\033[33m Jogo da adivinhação \033[m'))
computer = randint(0, 10)
palpite = False #Tive que mudar o valor dessa variável pois o computador poderia pensar em um número
contagem = 1 
while not palpite:
    jogador = int(input('Digite um número que você acha que o computador pensou entre 0 e 10:\033[32m '))
    if jogador != computer:
        print('\033[1;31mVocê errou!\033[m Tente novamente.')
        if palpite > computer:
            print('Tente um número menor')
        else:
            print('Tente um número maior')
        contagem += 1
    elif jogador == computer:
        palpite = True #Teve que ser adicionado por causa do valor do True
print(f'\033[1;32mParabéns! Você acertou!\033[m. Foram necessários \033[1;35m{contagem}\033[m palpites até acertar.')
