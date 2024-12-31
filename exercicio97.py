'''
Faça um programa que tenha uma função chamada escreva() que receba um
texto qualquer com parâmetro e mostre uma mensagem com tamanho adaptável.

Ex:
escreva('Olá, Mundo!')

Saída:
~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~
'''
def escreva(text):
    print('~' * (len(text) + 4))
    print(f'  {text}') # Antes foi usado text.center(2)
    print('~' * (len(text) + 4))
    

texto = str(input('Digite a sua mensagem: '))
escreva(texto)
# Funciona perfeitamente!