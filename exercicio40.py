nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
#calculando a nota:
result = (nota1 + nota2)/2
#resultado do aluno:
if result < 5.0:
    print('\033[41m REPROVADO \033[m média menor que 5.0')

elif result <= 5.0 or result <= 6.9:
    print('\033[43m RECUPERAÇÃO \033[m média {:.1f}'.format(result))

else:
    print('\033[44m APROVADO \033[m média do aluno {:.1f}'.format(result))
