'''
Faça um programa que tenha uma função chamada contador(), que recebe
três parâmetros, início, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1.
b) De 10 até 0, de 2 em 2.
c) Uma contagem personalidazda
'''
from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo = -passo
    elif passo == 0:
        passo = 1
    
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)
    if inicio < fim:
        for numbers in range(inicio, fim+1, passo):
            print(numbers, end=' ') 
            sleep(0.5)
        print('FIM!')
    if inicio > fim:
        for numbers in range(inicio, fim-1, -passo):
            print(numbers, end=' ')
            sleep(0.5)
        print('FIM!') 
  
    
a = contador(inicio=1, fim=10, passo=1)
b = contador(inicio=10, fim=0, passo=2)
# Contagem personalizada
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
c = contador(inicio=i, fim=f, passo=p)
# Funciona perfeitamente!
# Nas versões mais novas do pycharm, onde o professor está fazendo o exercício,
# a biblioteca time com o sleep está criando um buffer de tela. Ao invés de
# mostrar os números aparescendo, ele para no terminal e só quando o tempo do
# sleep acaba totalmente ele mostra o resultado. Modo de resolver: no print
# que antecede o sleep, coloque flush=True.
