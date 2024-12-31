def leiaInt(number=0):
    while True:
        number_ = input('Digite um número: ')
        try:
            number_ = int(number_)
            break
        except ValueError:
            print('\033[1;31mErro!\033[m \033[31mDigite um valor inteiro válido.\033[m')
    return number_
    
# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')