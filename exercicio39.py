from datetime import date
nome = str(input('Digite o seu nome: '))
ano = int(input('Digite o ano em que você nasceu: '))
anot = int(date.today().year)
result = anot - ano

if result == 18:
    print('Você tem \033[42m 18 anos \033[m, você deve servir ao exercito.')
    
elif result > 18:
    print('Você tem mais de \033[41m 18 anos \033[m. O prazo excedido foi há {} anos.'.format(result - 18))
    print('O seu alistamento foi em \033[33m{}\033[m'.format(anot - (result - 18)))
    
else:
    print('Você não tem \033[44m 18 anos \033[m para servir ao exercito. Espere {} anos.'.format(18 - result))
    print('O seu alistamento será em \033[33m{}\033[m'.format(anot + (18 - result)))
    