'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.
'''
def area(largura, comprimento):
    área = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {área}m².')


print(' Controle de Terrenos')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
# Funciona perfeitamente!
