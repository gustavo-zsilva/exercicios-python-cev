from math import hypot
co = float(input('Medida do cateto oposto: '))
ca = float(input('Medida do cateto adjacente: '))
print('-' * 27)
hipo = hypot(co, ca)
print('Sabendo que {} é o cateto oposto e {} é o cateto adjacente, a hipotenusa é {:.2f}.'.format(co, ca, hipo))






