def titleFunction(title):
    """_summary_
    Função responsável por criar um título apresentável para
    o programa
    Args:
        title (str): Title insert
    """
    
    mostrarLinha('-', 40)
    print(title.center(40))
    mostrarLinha('-', 40)
  
  
def colorFont(cor='limpar', text=''):
    """_summary_
    Função responsável por mudar a cor do texto que for inserido.
    Args:
        cor (str, optional): color font insert. Defaults to 'limpar'.
        text (str, optional): text insert. Defaults to ''.

    Returns:
        _type_: _description_
    """
    
    dictColor = {
        'limpar':'\033[m',
        'vermelho': '\033[31m',
        'amarelo': '\033[33m',
        'azul':'\033[34m'
    }
    return f'{dictColor[cor]}{text}{dictColor["limpar"]}'


def mostrarLinha(linhaCaracter, tamLinha):
    """Função que cria uma linha no terminal

    Args:
        linhaCaracter (str): Caractere que você quer que forme a linha
        tamLinha (int): Tamanho da linha
    """
    
    print(f'\033[1m{linhaCaracter}\033[m'*tamLinha)


def tratamentoError(option):
    vrfy = 0
    try:
        verify = int(option)
        vrfy = True
    except:
        vrfy = False
        
    if vrfy:
        return True
    else:
        return False