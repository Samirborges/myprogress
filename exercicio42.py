from time import sleep
r1 = int(input('Digite o primeiro valor de uma reta para um triângulo: '))
r2 = int(input('Digite o segundo valor de uma reta para um triângulo: '))
r3 = int(input('Digite o terceiro valor de uma reta para um triângulo: '))
#calculando retas:

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32mO valor das retas é suficiente para um triângulo \033[m')
    sleep(2)
    print('\033[33mAnalisando qual tipo de triângulo...\033[m')
    sleep(5)
    
    #Definindo qual tipo de triângulo
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('Essas são as medidas de um triângulo: \033[33mEquilátero\033[m')
    
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Essas são as medidas de um triângulo: \033[33mISÓSCELES\033[m')
    
    else:
        print('Essas são as medidas de um triângulo: \033[33mESCALENO\033[m')
        
else:
    print('\033[31mAs medidas que você digitou, não são suficiente para fazer um triângulo.\033[m')