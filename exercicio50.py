somator = 0
cont = 0
for num in range(1, 7):
    number = int(input('Digite um número: '))
    if number % 2 == 0:
        somator += number
        cont += 1
print(f'O número de números pares que você digitou foi {cont} e a soma entre eles é {somator}')