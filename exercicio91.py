from random import randint
from time import sleep
from operator import itemgetter
print('Valores sorteados:') #Sorteando os jogadores
jogadores = {
    'jogador1' : randint(1, 6),
    'jogador2' : randint(1, 6),
    'jogador3' : randint(1, 6),
    'jogador4' : randint(1, 6)
}
for k, v in jogadores.items(): # Imprimindo o resultado do sorteio
    print(f'    O {k} tirou {v}')
    sleep(1)
# Forma que eu tinha feito o exercício (funcional)
'''jogadores_visitados = jogadores.copy()
jogadores_determinados = cont = 0
print('Ranking dos jogadores:') # Imprimindo e posicionando os jogadores em um rank de acordo com os valores do sorteio. 
while jogadores_determinados != 4:
    for k, v in jogadores.items():
        sleep(1)
        maior = max(jogadores_visitados.values())
        while True:
            if v == maior:
                print(f'    {cont+1}° lugar: {k} com {v}')
                del jogadores_visitados[k]
                cont += 1
                jogadores_determinados += 1
            break'''
# Forma que o professor resolveu
ranking = list(sorted(jogadores.items(), key=itemgetter(1), reverse=True)) 
for rank in range(len(ranking)):
    sleep(1)
    print(f'    {rank+1}° lugar: {ranking[rank][0]} com {ranking[rank][1]}')
# 1. Usou o jogadores.items() para ordenar tanto os itens quanto as chaves do dicionário
# 2. Critério de ordenação, onde o sorted seria direcionado. Pois como ele possívelmente le as chaves...
#    colocou o valor das chaves sendo direcionados para os valores do dicionário usando a função operator...
#    itemgetter(0) - Para ler as chaves itemgetter(1) para ler os valores
# 3. reverse=True para ordenar do maior para o menor. 