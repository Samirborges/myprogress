# Inserindo informações do jogador:
jogador = dict()
jogador['nome'] = str(input('Digite o nome do jogador: ')).strip()
quant_partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
partidas_jogadas = list()

# Inserindo os gols do jogador em cada partida;
tot_gols = 0
for partidas in range(quant_partidas):
    partidas_jogadas.append(int(input(f'Quantos gols na partida {partidas}? ')))
    tot_gols += partidas_jogadas[partidas]
    
#Inserindo as informações dos gols no dicionário: jogador;
jogador['gols'] = partidas_jogadas
jogador['total'] = tot_gols

# Imprimindo todo o resultado dos dados inseridos;
print('\033[1m-=\033[m'*35)
print(jogador)
print('\033[1m-=\033[m'*35)

for key, values in jogador.items():
    print(f'O campo {key} tem o valor {values}')
print('\033[1m-=\033[m'*35)
print(f'O jogador {jogador['nome']} jogou {quant_partidas} partidas.')
for partidas in range(quant_partidas):
    print(f'{' ':<4}=> Na partida {partidas}, fez {partidas_jogadas[partidas]} gols.')
print(f'Foi um total de {jogador['total']} gols.')
