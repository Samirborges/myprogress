peso = float(input('Digite o seu peso Kg: '))
altura = float(input('Digite a sua altura m: '))
imc = peso/(altura * altura)
if imc < 18.5:
    print('''Seu IMC é de: {:.2f}, você está \033[1;41mABAIXO DO PESO!\033[m'''.format(imc))

elif imc > 18.5 and imc < 25:
    print('Seu IMC é de: {:.2f}. Você está no \033[1;42mPESO IDEAL!\033[m'.format(imc))

elif imc > 25 and imc < 30:
    print('Seu IMC é de: {:.2f}. Você está com \033[1;43mSOBREPESO!\033[m'.format(imc))

elif imc > 30 and imc < 40:
    print('Seu IMC é de: {:.2f}. Você está com \033[1;41mOBESIDADE!\033[m'.format(imc))

else:
    print('Seu IMC é de {:.2f}. Você está com \033[1;45mOBESIDADE MORBIDA!\033[m'.format(imc))
