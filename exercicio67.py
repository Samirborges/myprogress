while True:
    number = int(input('Quer ver a tabuada de qual valor? '))
    print(f'\033[1m-\033[m'*40)
    if number < 0:
        break    
    for c in range(1, 11):
        print(f'{number} x {c} = {number*c}')
    print(f'\033[1m-\033[m'*40)
print('FIM DO PROGRAMA')
