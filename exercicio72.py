while True:
    number = int(input('Digite um número de 0 a 20: '))
    if number < 0 or number > 20:
        while number < 0 or number > 20:
            number = int(input('Erro, tente novamente: Digite um número de 0 a 20: '))
    numberextense = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatoze', 'quinze', 'deseseis', 'desesete', 'desoito', 'desenove', 'vinte')
    print(f'Você digitou {numberextense[number]}')
    option = str(input('Você quer continuar?[S/N]: ')).upper()
    if option == 'N':
        break
