maior = 0
menor = 0
for p in range(0, 5):
    peso = float(input(f'Digite o peso da {p+1}° pessoa: '))
    if p == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'Maior peso lido {maior}Kg')
print(f'Menor peso lido {menor}Kg')
