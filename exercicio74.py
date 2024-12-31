from random import randint
number = randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)
'numbermax = numbermin = 0' # Com o uso do max() e do min() acada dispensando a declaração dessas variáveis
numberstr = str(number)
numberstr = numberstr.replace('(', '')
print(numberstr.replace(')', ''))

'''for c in range(0, 5):
    if c == 0:
        numbermax = numbermin = number[0]
    else:
        if number[c] > numbermax:
            numbermax = number[c]
        if number[c] < numbermin:
            numbermin = number[c]''' #Com o uso do max() e do min() acaba dispensando a estrutura de repetição para rotular de maior e menor número
            
print(f'O maior número é: {max(number)}')
print(f'O menor número é: {min(number)}')