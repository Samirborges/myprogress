nome = str(input('Nome: '))
média = float(input(f'Média de {nome}: '))
aluno = {
    'Nome': nome,
    'Média': média
}
if aluno['Média'] >= 7.0:
    situação = 'Aprovado(a)'
elif 5 <= aluno['Média'] < 7:
    situação = 'Recuperação'
else:    
    situação = 'Reprovado(a)'
aluno['Situação'] = situação
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
