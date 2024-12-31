from funcoesex115 import colorFont


def verifyFile():
    """_summary_
    Verificando se existe o arquivo
    Returns:
        void: None
    """
    
    try:
        with open('pessoascadastradas.txt', 'r', encoding='UTF-8'):
            None  
    
    except FileNotFoundError:
        with open('pessoascadastradas.txt', 'a', encoding='UTF-8') as people:
            # Inserindo dados
            people.write(f'{'Ana Paula Vieira':<30}{'32 anos':>3} \n')
            people.write(f'{'Cláudio Mendonça':<30}{'18 anos':>3} \n')
            people.write(f'{'Gustavo Gabriel':<30}{'41 anos':>3} \n')
            people.write(f'{'Maria Clara Peixoto':<30}{'65 anos':>3} \n')
            people.write(f'{'Maurício Souza':<30}{'19 anos':>3} \n')
            people.write(f'{'Nilce Pedrosa':<30}{'43 anos':>3} \n')
            people.write(f'{'Pedro Gonçalvez':<30}{'18 anos':>3} \n')
            people.write(f'{'Rafael Abulquerque':<30}{'38 anos':>3} \n')
            people.close()
    return None


def pessoasCadastradas():
    verifyFile()
    with open('pessoascadastradas.txt', 'r', encoding='UTF-8') as peopleRead:
        print(peopleRead.read())
        peopleRead.close()
    return None
    

def cadastrarPessoa():
    verifyFile()
    nome = str(input('Nome: '))
    while True:
        idade = (input('Idade: '))
        try:
            idade = int(idade)
        except:
            print(colorFont('vermelho', 'Erro: Digite um númeiro inteiro válido.'))
        else:
            nome1 = nome.split()
            nome1 = f'{nome1[0]} {nome1[-1]}'
            print(f'Novo cadastro de {nome1} adicionado.')
            break
    with open('pessoascadastradas.txt', 'a', encoding='UTF-8') as cadastro:
        cadastro.write(f'{nome:<30}{idade:>3} anos \n')
        cadastro.close()
        
    return None 
