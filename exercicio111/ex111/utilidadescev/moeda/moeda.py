def aumentar(value, porc, form=False):
    aum = value * (porc/100)
    value += aum
    if form: # Exercício 109
        value = moeda(value)
    
    return value


def diminuir(value, porc, form=False):
    dim = value * (porc/100)
    value -= dim
    if form:
        value = moeda(value)
    
    return value


def dobro(value, form=False):
    value *= 2
    if form:
        value = moeda(value)
    return value


def metade(value, form=False):
    value = value / 2
    if form:
       value = moeda(value)
    
    return value

# Exercicio 108
def moeda(value):
    value = str(f'{value:.2f}')
    return f'R${value.replace('.', ',')}'

#Exercício 110
def resumo(value, aumento, redução):
    print('\033[1m-\033[m'*30)
    print('RESUMO DO VALOR'.center(30))
    print('\033[1m-\033[m'*30)
    
    # Inserindo as informações para o resumo
    print(f'Preço análisado: \t{moeda(value)}')
    print(f'Dobro do preço: \t{dobro(value, True)}')
    print(f'Metade do preço: \t{metade(value, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(value, aumento, True)}')
    print(f'{redução}% de redução: \t{diminuir(value, redução, True)}')
    print('\033[1m-\033[m'*30)
    
    return None
    