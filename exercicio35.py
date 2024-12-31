r1 = float(input('Digite o valor de uma reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os valores que você digitou são suficiente para fazerem uma triângulo.')

else:
    print('Os valores que você digitou não são suficientes para fazerem um triângulo.')
