from time import sleep
salario = float(input('Digite o valor do seu salário: R$ '))
print('Calculando o seu aumento... ')
sleep(3)
if salario >= 1250.00:
    aumento = salario*0.10
    print('{:.2f}'.format(salario + aumento))
else:
    aumento = salario*0.15
    print('{:.2f}'.format(salario + aumento))
