contyear = contsexm = contsexf = 0
while True:
    '''person = str(input('Digite o nome da pessoa: '))'''
    year = int(input('Digite a idade: '))
    if year > 18: #Contador de pessoas que tem +18
        contyear += 1
    sex = str(input('Digite o sexo da pessoa[M/F]: ')).upper()[0]
    if sex == 'M':
        contsexm += 1
    if sex != 'M' and sex != 'F':
        while  sex != 'M' and sex != 'F':
            print('Sexo invalido')
            sex = str(input('Digite o sexo da pessoa [M/F]: ')).upper()[0]
    option = str(input(('Você quer cadastrar mais pessoas?[S/N]: '))).upper()[0] #Opção de escolher mais cadastro
    if sex == 'F' and year < 20:
        contsexf += 1
    if option == 'N':
        break
    if option != 'N' and option != 'S':
        while option != 'N' and option != 'S':
            option = str(input(('Você quer cadastrar mais pessoas?[S/N]: '))).upper()[0] #Opção de escolher mais cadastro
print(f'Existem {contyear} pessoas com mais de 18 anos')
print(f'Existem {contsexm} homens cadastrados')
print(f'Existem {contsexf} mulheres com menos de 20 anos')    
