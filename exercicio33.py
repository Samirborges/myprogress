#Código que eu escrevi:
'''n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
print('Analizando os números que você colocou...')

if (n1> n2 and n1> n3):
    print('Dentre os três números que você colocou, o número {} é maior.'.format(n1))
    
elif (n2> n1 and n2> n3):
    print('Dentre os três números que você colocou, o número {} é maior'.format(n2))
   
elif (n3> n1 and n3> n2):
    print('Dentre os três números que você colocou, o número {} é maior.'.format(n3))
   
else:
    print('Infelizmente o programador que escreveu isso aqui não é bom suficiente.')

if (n1< n2 and n1< n3):
    print('Dentre os três números que você colocou, o número {} é menor.'.format(n1))
    
elif (n2< n1 and n2< n3):
    print('Dentre os três números que você colocou, o número {} é menor'.format(n2))
   
elif (n3< n1 and n3< n2):
    print('Dentre os três números que você colocou, o número {} é menor.'.format(n3))

else:
    print('Infelizmente o programador que escreveu isso aqui não é bom suficiente.')'''

#Código que o professor fez:
a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Digite o terceiro número: '))
#Verificando o menor número:
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('Menor número: {}'.format(menor))
print('Maior número: {}'.format(maior))
