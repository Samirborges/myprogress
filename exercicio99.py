from time import sleep
'''
Faça um programa que tenha uma função chamada maior (), que receba vários
parâmetros com valores interios.

Seu programa tem que analisar todos os valores e dizer qual deles é 
maior.
'''

def mostrar_linha():
    print('-='*30)


def maior(*list_numbers):
    mostrar_linha()
    print('Analisando os valores passados...')
    for number in list_numbers:
        print(number, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(list_numbers)} valores ao todo.')
    
    # Analisando qual desses valores é maior
    number_maior = 0
    if list_numbers != 0:
        for maior in range(len(list_numbers)):
            if maior == 0:
                number_maior = list_numbers[0]
            else:
                if number_maior < list_numbers[maior]:
                    number_maior = list_numbers[maior]
    print(f'O maior valor informado foi {number_maior}.')
    return None


value = maior(2, 9, 4, 5, 7, 1)
value = maior(4, 7, 0)
value = maior(1, 2)
value = maior(6)
value = maior()
# Funciona perfeitamente!