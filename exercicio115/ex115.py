from funcoesex115 import titleFunction, colorFont, mostrarLinha, tratamentoError
from bancoDeDados import pessoasCadastradas, cadastrarPessoa

# Programa principal - Sistema modularizado de cadastro e consulta
while True:
    titleFunction('MENU PRINCIPAL')

    # Menu do software: Uma coisa diferente é que ele criou uma lista de menus para poder criar as opções de menu pelo próprio programa e já está apresentável para o usuário
    print(f'''{colorFont('amarelo', '1')} - {colorFont('azul', 'Ver pessoas cadastradas')} \n{colorFont('amarelo', '2')} - {colorFont('azul', 'Cadastrar nova Pessoa')} \n{colorFont('amarelo', '3')} - {colorFont('azul', 'Sair do Sistema')}''')

    mostrarLinha('-', 40)
    while True:
        option = input(f'{colorFont('amarelo', 'Sua opção: ')}')
        verifyError = tratamentoError(option)
        if verifyError == True:
            option = int(option)
            break
        elif verifyError == False:
            print(f'{colorFont('vermelho', 'ERRO: por favor, digite um número inteiro válido.')}')
        
    # Funções do sistema à serem executados: 
    if option == 1:
        titleFunction('PESSOAS CADASTRADAS')
        pessoasCadastradas()
        
    elif option == 2:
        titleFunction('NOVO CADASTRO')
        cadastrarPessoa()
    elif option == 3:
        titleFunction('Saindo do sistema... Até logo!')
        break
    else:
        print(colorFont('vermelho', 'Erro! Digite uma opção válida.'))
