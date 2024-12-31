def ficha(nome='<desconhecido>', gols=0):
    if nome == '':
        nome = '<desconhecido>'
    
    if gols == '':
        gols = 0
        
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    
    
# Programa principal
name = str(input('Nome do jogador: '))
number_goal = str(input('Número de gols: '))
ficha(name, number_goal)