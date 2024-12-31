def notas(*nota, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação do aluno.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    
   # Calculando a média; Maior e menor nota
    num = 0
    for n in range(len(nota)):
       num += nota[n]
       # Encontrando a maior e menor nota:
       maior_menor = maiorMenor(nota)
    media = num/len(nota)
   
   # Fazendo o boletim
    boletim = {
        'total': len(nota),
        'maior': maior_menor[0],
        'menor': maior_menor[1],
        'média': media
   }
   
   # Adicionando a situação do aluno
    if sit == True:
       if media >= 7:
           situação = 'APROVADO'
       
       elif media >= 6:
           situação = 'RAZOÁVEL'
           
       elif media <= 5:
           situação = 'REPROVADO'
        
       boletim['situação'] = situação
   
    return boletim


def maiorMenor(list_number):
    for n in range(len(list_number)):
        if n == 0:
           maior = list_number[n]
           menor = list_number[n]
        else:
           if maior < list_number[n]:
               maior = list_number[n]
           if menor > list_number[n]:
               menor = list_number[n]
    return maior, menor


resp = notas(3.5, 2, 6.5, 7, 4, sit=True)
print(resp)
print(help(notas))