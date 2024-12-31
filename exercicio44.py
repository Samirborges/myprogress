valor = float(input('Digite o preço do produto: R$ '))
print('''À vista dinheiro/cheque (1);
À vista no cartão (2);
2x no cartão (3);
3x ou mais no cartão (4);''')
pagamento = str(input('Qual vai ser a forma de pagamento? '))

if pagamento == '1':
    print('Você escolheu: \033[1;33mÀ vista no dinheiro/cheque\033[m')
    print('Valor a ser pago: \033[1;32mR$ {:.2f}\033[m'.format(valor - (valor * 0.1)))

elif pagamento == '2':
    print('Você escolheu: \033[1;33mÀ vista no cartão\033[m')
    print('Valor a ser pago: \033[1;32mR$ {:.2f}\033[m'.format(valor - (valor * 0.05)))
    
elif pagamento == '3':
    print('Você escolheu:\033[1;33m 2x no cartão\033[m')
    print('Preço a ser pago: R$ \033[1;32m{:.2f}\033[m'.format(valor))
    print('Valor de cada parcela: R$ \033[1;32m{:.2f}\033[m'.format(valor/2))

elif pagamento == '4':
    parcelas = int(input('Parcelas: '))
    if parcelas <= 2:
        print('\033[1;31mOpção invalida, tente novamente.\033[m')
    else:
        print('Você escolheu:\033[1;33m 3x ou mais no cartão\033[m')
        print('Valor a ser pago:\033[1;32m R$ {:.2f}\033[m'.format(valor + (valor * 0.2)))
        print('Valor a ser pago por cada parcela:\033[1;32m R$ {:.2f}\033[m'.format((valor + (valor * 0.2))/parcelas))

else: 
    print('\033[1;31mOpção invalida \033[m')
