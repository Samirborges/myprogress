ptm = int(input('Digite o primeiro termo: '))
progress = int(input('Digite a progressão aritimétrica: '))
c = i = 1
while c <= 10: #O professor colocou o valor ser diferente de zero, onde essa variável poderia ser mudado quando o programa pede quais termos a mais ele quer que mostre.
    print(f'{ptm} -> ', end='')
    ptm += progress
    c += 1
print('PAUSA')
i = int(input('Digite quantos termos deve apareçer: '))
conti = 0
if i != 0:  
    while i != 0:
        c = 1
        while c <= i:
            print(f'{ptm} -> ', end='') 
            ptm += progress
            c += 1
        print('PAUSA')
        conti += i
        i = int(input('Digite quantos termos deve apareçer: '))
print('Progressão finalizada com {} termos mostrados.'.format(conti+10))
