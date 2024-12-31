def voto(year):
    actual_year = 2018
    year_voto = actual_year - year
    
    if year_voto >= 65:
        print(f'Com {year_voto} anos: o voto é  OPCIONAL.')
    
    elif year_voto >= 18:
        print(f'Com {year_voto} anos: o voto é OBRIGATÓRIO')
    
    else:
        print(f'Com {year_voto} anos: o voto é NEGADO.')


# Programa principal
print('-'*20)
eleitor = int(input('Em que ano você nasceu? '))
voto(eleitor)
