print('{:=^40}'.format('Sequência de Fibonacci'))
terms = int(input('Digite quantos termos você que: '))
cont = 0
num = 0
ant = 1
print('0 → ', end='')
while cont <= terms - 2:
    result = ant + num
    ant = num
    num = result
    cont += 1
    print(f'{result} → ', end='')
print('FIM')
