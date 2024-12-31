num = int(input('Digite um número inteiro: '))
number = str(num)

if '2' in number[-1]:
    print('O número {} é Par'.format(num))

elif '4' in number[-1]:
    print('O número {} é Par'.format(num))

elif '6' in number[-1]:
    print('O número {} é Par'.format(num))

elif '8' in number[-1]:
    print('O número {} é Par'.format(num))

else:
    print('O número {} é Ímpar'.format(num))