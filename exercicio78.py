number = list()
for c in range(0, 5):
    number.append(int(input(f'Digite um valor para Posição {c}: ')))

numbercontmax = list(number[:])
numbercontmin = list(number[:])
print('-='*25)
print(f'Você digitou os valores {number}')

print(f'O maior valor digitado foi {max(number)} nas posições {number.index(max(number))}...', end='')
contmax = 1
while True:
    maxnumber = max(numbercontmax)
    numbercontmax.pop(numbercontmax.index(maxnumber))
    if str(maxnumber) in str(numbercontmax):
        print(f' {numbercontmax.index(maxnumber)+contmax}...', end='')
        contmax += 1
    else:
        break

print(f'\nO maior valor digital foi {min(number)} nas posições {number.index(min(number))}...', end='')
contmin = 1
while True:
    minnumber = min(numbercontmin)
    numbercontmin.pop(numbercontmin.index(minnumber))
    if str(minnumber) in str(numbercontmin):
        print(f' {numbercontmin.index(minnumber)+contmin}...', end='')
        contmax += 1
    else:
        break
  