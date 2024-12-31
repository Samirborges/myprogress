priceby = cont = contprodut = produtobarato = princebr = 0
while True:
    name_produt = str(input('Digite o nome do produto:\033[1;33m '))
    price = float(input('\033[mDigite o preço do produto: \033[1;32mR$'))
    priceby += price #Calculando o total da compra
    if price > 1000: #Contando quantos produtos custa mais de R$1000,00
        cont += 1
    contprodut += 1 #Contador de produtos 
    '''if contprodut == 1: #Mecanismo para definir o primeiro produto como o mais barato
        produtobarato = name_produt
        pricebr = price
    else: #Mecanismo para calcular qual é o produto mais barato
        if price < pricebr: #Caso o preço do produto for menor do que o preço mais barato definido anteriormente...
            produtobarato = name_produt #O produto mais barato recebe o nome
            pricebr = price #E o produto recebe um novo preço'''
    if contprodut == 1 or price < princebr:
        produtobarato = name_produt
        pricebr = price
    option = str(input('\033[mVocê quer continuar?[S/N] ')).upper()[0] #Escolher se vai cadastrar mais produto
    if option != 'N' and option != 'S': #Mecanismo para decifrar a resposta
        while option != 'N' and option != 'S':
            option = str(input('Opção invalida! Você quer continuar [S/N]: ')).upper()[0]
    if option == 'N': #Condição de parada
        break
print(f'O valor total da compra é \033[1;32mR${priceby:.2f}\033[m')
print(f'Na sua compra existem \033[1;33m{cont}\033[m produtos que custam mais de \033[1;32mR$1000,00\033[m.')
print(f'O nome do produto mais barato é: \033[1;45m{produtobarato}\033[m que custa \033[1;32mR${pricebr:.2f}\033[m.')
 