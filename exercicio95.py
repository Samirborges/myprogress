# Inserindo informações do jogador:
jogador = dict()
jogadores = dict()
numero_jogador = 0
while True:
    print('\033[1m-\033[m'*30)
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
    
    numero_jogador += 1 # Finalizando as informações do jogador.
    
    jogadores[numero_jogador] = jogador.copy()
    #Opção para parar de adicionar jogadores:
    option = str(input('Você quer continuar? [S/N] ')).lower()[0]
    if option == 'n':
        break
    
# Imprimindo o resultado das informações dos jogadores
print('\033[1m-=\033[m'*35)
print(f'cod nome{' ':>10}gols{' ':>10}total ')
print('\033[1m-\033[m'*37)

for number_players in jogadores.keys():
    print(f'{' ':<3}{number_players} {jogadores[number_players]['nome']}{' ':<4}{jogadores[number_players]['gols']}{' ':<4}{jogadores[number_players]['total']}')
print('\033[1m-\033[m'*37)

# Escolha para mostrar dados detalhados do jogador:
while True:
    dados_jogador = int(input('Mostrar dados de qual jogador? '))
    if dados_jogador == 999:
        print('<< VOLTE SEMPRE >>')        
        break
    
    elif dados_jogador not in list(jogadores.keys()):
        print(f'ERRO! Não existe jogador com código {dados_jogador}! Tente novamente')
        print('\033[1m-\033[m'*37)
    else:
        # Imprimindo as informações detalhadas do jogador escolhido:
            print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[dados_jogador]['nome']}: ')

            for gols in range(len(jogadores[dados_jogador]['gols'])):
                print(f'{' ':>4} No jogo {gols} fez {jogadores[dados_jogador]['gols'][gols]} gols.')
            print('\033[1m-\033[m'*37)
