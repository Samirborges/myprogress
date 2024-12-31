frase = str(input('Digite uma frase: ')).lower()
frasejunt = ''.join(frase.split())
if frasejunt[::-1] == frasejunt:
    print('A frase que você digitou fica assim:')
    print('\033[33m{}\033[m A sua frase é um \033[34mpalíndromo \033[m'.format(frasejunt[::-1]))
else:
    print('A sua frase que você digitou fica assim: ')
    print('\033[33m{}\033[m A sua frase \033[31mnão\033[m é um políndromo'.format(frasejunt[::-1]))
