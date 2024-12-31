cont = soma = num = 0
num = int(input('Digite qualquer número inteiro ou \033[1;31m[999]\033[m para parar: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite qualquer número inteiro ou \033[1;31m[999]\033[m para parar: '))
print('A soma entre os números é \033[1;36m{}\033[m, e você digitou \033[1;35m{}\033[m números ao todo.'.format(soma, cont))
 