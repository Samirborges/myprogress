matriz = []
linha = 0
value = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz.append(int(input(f'Digite um valor para [{i}, {j}]: ')))

for c in range(0,3):
    print(f'[{matriz[c+linha]:^5}] [{matriz[c+(linha+1)]:^5}] [{matriz[c+(linha+2)]:^5}]')
    linha+=2
    
for pares in range(0,9):
    if matriz[pares] % 2 == 0:
        value += matriz[pares]
        
soma_terceira_coluna = matriz[2] + matriz[5] + matriz[8]

maior_second_line = matriz[3]

if matriz[4] > maior_second_line:
    maior_second_line = matriz[4]
    
if matriz[5] > maior_second_line:
    maior_second_line = matriz[5]

print(f'A soma de todos os valores pares digitados foram: {value}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_second_line}')
