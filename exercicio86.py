matriz = []
linha = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz.append(int(input(f'Digite um valor para [{i}, {j}]: ')))

for c in range(0,3):
    print(f'[{matriz[c+linha]:^5}] [{matriz[c+(linha+1)]:^5}] [{matriz[c+(linha+2)]:^5}]')
    linha+=2
