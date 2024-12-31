cont = soma = number = 0
while True:
    number = int(input('Digite qualquer número inteiro ou \033[1;31m[999]\033[m para parar: '))
    if number == 999:
        break
    cont+=1
    soma += number
print(f'A soma dos \033[1;33m{cont}\033[m valores é \033[1;35m{soma}\033[m.')
