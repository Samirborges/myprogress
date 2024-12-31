cont = media = 0
option = str('A')
while option != 'NÃO' and option != 'N':
    num = int(input('Digite um número: '))
    option = str(input('Você quer continuar?[SIM/NÃO]: ')).upper()
    cont += 1
    media += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'Você digitou \033[36m{cont}\033[m números e a média foi \033[1;35m{media/cont}\033[m.')
print(f'O maior número foi \033[1;31m{maior}\033[m e o menor número foi \033[1;33m{menor}\033[m.')
