vl = int(input('Velocidade do carro (Km/h): '))
if vl > 80:
    multa = float((vl-80)*7)
    print('O carro foi multado por andar: {}Km/h. A multa vai custar: R${:.2f}'.format(vl, multa))
else:
    print('Tá de boa, não precisa se preocupar.')