from random import randint
from time import sleep
'''
Faça um programa que tenha uma lista chamada números e duas funções 
chamadas sorteia() e somaPar(). Aprimeira função vai sortear 5 números 
e vai colocá-los dentro da lista e a segunda vai mostrar a soma entre 
todos os valores PARES sorteados pela função anterior.
'''
def sorteia():
    numbers = list()
    print('Sorteando 5 valores da lista:', end=' ')
    for sorteio in range(0, 5):
        value = randint(1, 10)
        numbers.append(value)
        sleep(0.5)
        print(value, end=' ')
    print('PRONTO!')
    return numbers


def somaPar(lista_sorteio):
    print(f'Somando os valores pares de', end='')
    colorindo_numeros(lista_sorteio)
    print(', temos', end=' ')
    
    # Verificando os números pares dentro da lista de sorteio
    somatório = 0
    for num in range(5):
        if lista_sorteio[num] % 2 == 0:
            somatório += lista_sorteio[num]
    print(somatório)
    
    
def colorindo_numeros(numers):
    for num in numers:
        if num % 2 == 0:
            print(f' \033[1;33m{num}\033[m', end='') 
        else:
            print(f' \033[1;31m{num}\033[m',end='')  


sorteio = sorteia()
somaPar(sorteio)
# Funciona perfeitamente!