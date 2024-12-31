from datetime import date
maidade = 0
meidade = 0
for year in range(0, 7):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(year+1)))
    if date.today().year - ano < 18:
        meidade += 1
    else:
        maidade += 1
print('Quantidade de pessoas \033[32mMaior de idade\033[m {}'.format(maidade))
print('Quantidade de pessoas que é \033[33mMenor de idade\033[m {}'.format(meidade))
