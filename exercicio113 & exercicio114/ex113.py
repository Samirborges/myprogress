# Desafio 104
def leiaInt(number=0):
    while True:
        number_ = input('Digite um número: ')
        try: # No desafio 104, isso não era para está aqui, e sim um isnumeric()
            number_ = int(number_)
            break
        except (ValueError, KeyboardInterrupt, TypeError):
            print('\033[1;31mErro!\033[m \033[31mDigite um valor inteiro válido.\033[m')
    
    return number_


def leiaFloat(floatNumber=0):
    while True:
        floatNumber = input('Digite um número Real: ')
        try:
            floatNumber = float(floatNumber)
            break
        except KeyboardInterrupt: # Não consegui botar essa função do keyboard
            print('O usuário preferiu não digitar esse número.')
            
        except Exception:
            print('\033[1;31mErro!\033[m \033[31mTipo de dado inválido. Digite um valor flutuante válido.\033[m')
    return floatNumber    

# Programa principal
n = leiaInt('Digite um número: ')
f = leiaFloat('Digite um número Real: ')
print(f'Você digitou os números {n} e {f}.')
