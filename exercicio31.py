dist = int(input('Digite a distância da sua viagem: '))
if dist <= 200:
    preço = float(dist*0.50)
    print('O preço da passagem vai ser R${:.2f}'.format(preço))
else:
    preço = float(dist*0.45)
    print('O preço da passagem vai ser R${:.2f}'.format(preço))