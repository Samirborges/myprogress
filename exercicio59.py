number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))
option = 0
while option != 5:
    print('''Qual opção você quer escolher?
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    option = int(input('Sua opção: '))
    if option == 1:
        print(f'O resultado de: {number1} + {number2} = {number1 + number2}')
    elif option == 2:
        print(f'O resultado de: {number1} * {number2} = {number1*number2}')
    elif option == 3:
        if number1 > number2:
            print('Dentre os números que você digitou, {} é maior que {}.'.format(number1, number2))
        else:
            print('Dentre os números que você digitou, {} é maior que {}.'.format(number2, number1))
    elif option == 4:
        number1 = int(input('Digite o primeiro número: '))
        number2 = int(input('Digite o segundo número: '))
    elif option != 5:
        print('\033[1;31mOpção inválida.\033[m Tente novamente.')
    print('=-=='*10) 