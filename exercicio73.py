campeões = ('Corithians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruseiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO' )
print('-='*15)

print(f'Os primeiro cinco colocados são: ', end='') # Resposta A: Nome dos times dos cinco primeiros colocados
print(f'{campeões[0:5]}')

print('-='*15)

print(f'Os quatro ultimos colocados são: ', end='') # Resposta B: Nome dos ultimos colocados
print(f'{campeões[16: 20]}, ')

print('-='*15)

print(f'Os nomes dos times em ordem alfabética: {sorted(campeões)}') # Resposta c: Nomes em ordem alfabética

print('-='*15)

print(f'A posição da Chapecoense está na {campeões.index('Chapecoense')+1}° posição.')
print('-='*15)
