from datetime import datetime
trabalhador = dict()


# Inserindo as informações do trabalhador
trabalhador['nome'] = str(input('Nome: ')).strip()
ano_nascimento = int(input('Ano de Nascimento: '))
carteira_trabalho = int(input('Carteira de Trabalho (0 não tem): '))

idade = datetime.now().year - ano_nascimento
trabalhador['idade'] = idade
trabalhador['ctps'] = carteira_trabalho

# Verificando o número da carteira de trabalho:
if carteira_trabalho == 0:
    None

else:
    ano_contratação = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Digite o salário: \033[32;1mR$ '))
    aposentadoria = (ano_contratação - ano_nascimento) + 35
    trabalhador['contratação'] = ano_contratação
    trabalhador['apasontadoria'] = aposentadoria

# Tratamento dos dados:    
print('\033[m-='*35)

for keys, value in trabalhador.items():
    print(f'{keys} tem o valor {value}')
