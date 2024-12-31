from time import sleep
vcasa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o valor do seu salário: R$ '))
anos = int(input('Quantos anos você pretende pagar? '))
print('Calculando valor do emprestimo...')
sleep(5)
vparcelas = vcasa/(anos*12)
psalario = salario*0.3

if vparcelas < psalario:
    print('\033[42mEmprestimo aprovado! \033[m')
    print('Valor das parcelas R$\033[33m {:.2f}\033[m'.format(vparcelas))
else:
    print('\033[41mO emprestimo foi negado. \033[m')
    print('O valor das parcelas excedeu o valor das parcelas.')
    print('A prestação será de R$\033[33m{:.2f}\033[m'.format(vparcelas))
