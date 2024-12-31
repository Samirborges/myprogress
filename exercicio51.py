print('='*20)

print('PROGREÇÃO ARITIMÉTRICA')

print('='*20)

pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
for number in range(pt, 10*razao, razao):
    print(number, ' ->' , end=' ')

print('ACABOU')
