cadas_pessoas = dict()
pessoas = dict()
number_people = media = 0
lista_de_mulheres = list()
while True:
    # Inserindo as informações das pessoas para o cadastro;
    cadas_pessoas['nome'] = str(input('Nome: ')).strip()
    cadas_pessoas['sexo'] = str(input('Sexo [M/F] ')).strip().upper()
    
    #Mecanismo de verificação de resposta.
    while True:
        if cadas_pessoas['sexo'] not in 'M' and cadas_pessoas['sexo'] not in 'F':
            print('Erro! Por favor, digite apenas M ou F.')
            cadas_pessoas['sexo'] = str(input('Sexo [M/F] ')).strip().upper()
        else:
            break 
    
    cadas_pessoas['idade'] = int(input('Idade: '))
    number_people += 1
    
    pessoas[f'Pessoa: {number_people}'] = cadas_pessoas.copy()
    media += cadas_pessoas['idade']
    
    # Colocando as mulheres em uma lista:
    if cadas_pessoas['sexo'] == 'F':
        lista_de_mulheres.append(cadas_pessoas['nome'])

        
    while True:
        option = str(input('Quer continuar? [S/N] ')).strip().lower()
        
        #Verificando a resposta:
        if option == 'n':
            break
        
        elif option == 's':
            break
            
        else:
            print('Erro! Responda apenas S ou N.')
        
    if option == 'n':
        break
    if option == 's':
        None
        

# Realizando o calculo da média das pessoas cadastradas:
media = media/number_people

print('\033[1;33m-=\033[m'*35)

# Imprimindo os resultados dos cadastros:
print(f'- O grupo tem {number_people} pessoas.')
print(f'- A média de idade é de {media} anos.')
print('- As mulheres cadastradas foram:', end=' ')
for mulheres in range(len(lista_de_mulheres)):
    print(lista_de_mulheres[mulheres], end=' ')
print('\n- Lista de pessoas acima da média')

# Imprimindo a lista de pessoas com idade a cima da média:
for cont in range(len(pessoas.keys())):
    if pessoas[f'Pessoa: {cont+1}']['idade'] > media:
        print(f'\nnome = {pessoas[f'Pessoa: {cont+1}']['nome']}; sexo = {pessoas[f'Pessoa: {cont+1}']['sexo']}; idade = {pessoas[f'Pessoa: {cont+1}']['idade']};\n')
print('<< ENCERRADO >>')
