s = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Dígite o {c} número: '))
    if n% 2== 0:
        s += n
        cont += 1

print(f'Você informou {cont} e a soma {s}')
