num = int(input('Digite um número para ver a sua tabuada: '))
s = 0
for c in range(0, 10):
   print('{} X {} = {}'.format(num, c+1, num*(c+1)))