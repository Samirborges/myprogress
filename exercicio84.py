galera = list()
pessoas_pesadas = pessoas_leves = 0
quant_pessoas_cadastradas = 0

#Impute de entrada dos dados das pessoas
while True:
    galera.append(str(input('Nome: ')))
    galera.append(float(input('Digite o seu peso: ')))
    
    quant_pessoas_cadastradas += 1
    
    option = str(input('Você quer continuar? [s/n]: ')).lower()
    if option == 'n':
        break
    
# Configuração das pessoas mais pesadas e das pessoas mais leves.
print('\033[1m-=\033[m'*30)
print(f'A quantidade de pessoas cadastradas é: {quant_pessoas_cadastradas}')
pessoas_pesadas = max(galera[1::2])
pessoas_leves = min(galera[1::2])
print(f'O maior peso foi de {pessoas_pesadas} Peso de ', end='')

# Encontrando e printando as pessoas com seus pesos pesados e leves.
for c in galera:
    if pessoas_pesadas in galera:
        find_pesadas = galera.index(pessoas_pesadas)
        print(galera[find_pesadas-1])
        galera.pop(find_pesadas)
        galera.pop(find_pesadas-1)

print(f'O menor peso foi de {pessoas_leves}. Peso de ', end='')
for i in galera:
    if pessoas_leves in galera:
        find_leves = galera.index(pessoas_leves)
        print(galera[find_pesadas-1])
        galera.pop(find_leves)
        galera.pop(find_leves-1)
