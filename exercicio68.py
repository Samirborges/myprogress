from random import randint
player = choesen = cont = 0 #Setando as variáveis
print('=-'*40)
print('VAMOR JOGAR PAR OU ÍMPAR')
print('=-'*40)
while True:
    player = int(input('Digite um número: ')) #Escolha do número do jogador
    choesen = str(input('Par ou Ímpar [P/I]: ')).upper() #Escolha de par ou ímpar
    computer = randint(1, 10) # Sorteio do computador
    print(f'Você jogou {player} e o computador {computer}. Total de {player + computer}', end=' ')
    if (player + computer) % 2 == 0:
        print('PAR')
    else:
        print('IMPAR')
    if (player + computer) % 2 == 0 and choesen == 'P' or (player + computer) % 2 == 1 and choesen == 'I': #Calculo do resultado
        print('\033[1;42mVocê venceu!\033[m') #Caso o jogador vencer
        cont += 1
    else:
        print('\033[1;41mVocê perdeu!\033[m') #Caso o jogador perder
        break
    print('Vamos de novo...')
if cont > 1: # Mensagem caso o jogador ganhe mais de uma vez
    print(f'Você venceu \033[1;32m{cont}\033[m consecutivamente.')
elif cont == 1: # Mensagem caso o jogador ganhe apenas uma vez
    print(f'Você venceu apenas \033[1;33m1\033[m vez...')
