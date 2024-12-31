listnumber = list()
while True:
    input_listnumber = int(input('Digite um valor: '))
    
    if input_listnumber in listnumber:
        print('Valor duplicado! Não vou adicionar...')    
    
    else:
        listnumber.append(input_listnumber)
        print('Valor adicionado com sucesso...')
    
    option = str(input('Quer continuar? [S/N] ')).upper()
    if 'N' in option:
        break
print(f'Você digitou os valores {sorted(listnumber)}')
