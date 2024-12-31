w = 0
listagem = ('Lápis', '1.75', 'Borracha', '2.00',  'Caderno', '15.90', 'Estojo', '25.00', 'Transferidor', '4.20', 'Compasso', '9.99', 'Mochila', '120.32', 'Canetas', '22.30', 'Livro', '34.90')
print('\033[1m-\033[m'*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('\033[1m-\033[m'*40)
for c in range(0, 9): #No separador o professor colocou de uma forma e que só aparecesse os nomes dos produtos quando o número fosse par
    separador = 29 - len(listagem[w]) #O separador foi colocado dessa forma print(f'listagem[c]:.<30. Ele vai preencher 30 caracteres com pontinhos no total.')
    separadornum = 7 - len(listagem[w+1]) # O separador do número foi colocado para ser alinhado a esquerda. print(f'listagem[c]:>7.2f. No caso esse print está dentro do else. Caso ele não seja impar.)
    print(f'{listagem[w]}{'.'*separador}R${' '*separadornum}{listagem[w+1]}')
    w += 2
print('\033[1m-\033[m'*40)
