name_list = list()
notas_list = list()
alunos = list()

cont = 0
while True:
    name_list.append(str(input('Nome: ')))
    notas_list.append(float(input('Nota 1: ')))
    notas_list.append(float(input('Nota 2: ')))
    cont += 1
    
    name_list.append(notas_list[:])
    notas_list.clear()
    
    alunos.append(name_list[:])
    name_list.clear()
    
    option = str(input('Você quer continuar? [S/N] ')).lower()
    if option == 'n':
        break
print(f'{"No":<4}.{"NOME":<10}{"MÉDIA":>8}')
for c in range(0, cont):
    nota1 = alunos[c][1][0]
    nota2 = alunos[c][1][1]
    média = (nota1+nota2)/2
    
    separador_nome =  3
    separador_média = 8 - (len(alunos[c][0])-3) 
    média = f'{média :.1f}'
    print(f'{c:<4} {alunos[c][0]:<10} {média:>8} ')

while True:
    select_student = int(input('Mostrar as notas de qual aluno? \033[1;31m [999]\033[m interrompe: '))
    if select_student == 999:
        break
    print(f'Notas de {alunos[select_student][0]} são {alunos[select_student][1]}\n')
