s = 0
c = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        s += num
        c += 1

print(f'A soma de todos os {c} valores solicitados é {s}')