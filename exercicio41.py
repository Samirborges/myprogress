from datetime import date
ano = int(input('Digite a data do seu nascimento: '))
cal = date.today().year - ano
if cal <= 9:
    print('Você está na categoria: \033[1;7m MIRIM \033[m')

elif cal <= 14:
    print('Você está na categoria: \033[1;44m INFANTIL \033[m')

elif cal <= 19:
    print('Você está na categoria: \033[1;43m JUNIOR \033[m')
    
elif cal <= 25: 
    print('Você está na categoria: \033[1;45m SÊNIOR \033[m')

else:
    print('Você está na categoria: \033[1;41m MASTER \033[m')