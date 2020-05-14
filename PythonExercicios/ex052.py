num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end = ' ')
        tot += 1
    else:
        print('\033[31m', end = ' ')
    print(c, end=' ')
if tot == 2:
    print('\n\033[mO número {} foi divisível {} vezes, portanto ele é um número primo.'.format(num, tot))
else:
    print('\n\033[mO número {} foi divisível {} vezes, portanto não é um número primo.'.format(num, tot))
