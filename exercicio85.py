listnumber = [[], []]

#Separando os números pares dos números ímpares
for c in range(0,7):
    number = int(input(f'Digite o {c+1}° número: '))
    if number % 2 == 0:
        listnumber[0].append(number)
    else:
        listnumber[1].append(number)

print(f'Os números pares digitados foram: {sorted(listnumber[0])}')
print(f'Os números ímpares digitados foram {sorted(listnumber[1])}')
