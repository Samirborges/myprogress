num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
if num1 > num2:
    print('Analisando os números que você digitou, conclui-se que. O número maior é {} e o menor é {}.'.format(num1, num2))
    
elif num2 > num1:
    print('Analisando os números que você digitou, conclui-se que. O número maior é {} e o menor é {}.'.format(num2, num1))
    
else:
    print('Não existe número maior nem menor, os dois são iguais.')