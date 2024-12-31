def fatorial(number, show):
    """
        -> Calcula o Fatorial de um número.
        :param number: O número a ser calculado.
        :param show: (opcional) Mostra ou não a conta.
        :return: O valor do Fatorial de um número n.  
    """
    # Calculando o fatorial
    result = 1
    for fact in range(number, 0, -1):
        result *= fact
        
        if show == True:
            if fact != 1:
                print(f'{fact} x', end=' ')
            if fact == 1:
                print(f'{fact} = ', end='')
    print(result)
    
    
fatorial(5, False)
help(fatorial)