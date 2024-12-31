def titulo(title, color, brek='\033[m'):
    print(color)
    print('~'*(len(title)+4))
    print(title.rjust(4, ' '))
    print('~'*(len(title)+4), end='')
    print(brek)
    

def help_(command):
    print('\033[7m')
    print(help(command))
    print('\033[m')
    
# Programa principal
while True:
    titulo('    SISTEMA DE AJUDA PyHELP    ', '\033[7;32m')
    prompt = str(input('Função ou Biblioteca > '))
    if prompt == 'fim':
        titulo('    ATÉ LOGO!   ', '\033[7;31m')
        break
    titulo(f"    Acessando o manual de comando '{prompt}'    ", '\033[7;34m')
    help_(prompt)