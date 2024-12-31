def aumentar(value, porc):
    aum = value * (porc/100)
    return value + aum


def diminuir(value, porc):
    dim = value * (porc/100)
    return value - dim


def dobro(value):
    return value * 2


def metade(value):
    return value / 2


# Exercício 108
def moeda(value):
    value = str(f'{value:.2f}')
    return f'R${value.replace('.', ',')}0'