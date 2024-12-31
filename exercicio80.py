number = list()
for c in range(0,5):
    number_input = int(input('Digite um número: '))
    if c == 0:
        number.insert(0, number_input)
        print('Número adicionado no final da fila...')
    else:
        if number_input > number[-1]:
            number.append(number_input)
            print('Número adicionado no final da fila...')
        
        else:
            for i in range(len(number)):
                if number_input < number[i]:
                    number.insert(i, number_input)
                    print(f'Número adicionado na posição {i}')
                    break
print('-='*45)
print(f'Os valores digitados em ordem foram {number}')
