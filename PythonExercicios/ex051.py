print('-=' * 20)
print('10 TERMOS DE UMA PA')
print('-=' * 20)
pt = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
decimo = pt + (10 - 1) * raz
for c in range(pt, decimo + raz, raz):
    print(c, end=' --> ')
print('ACABOU')
