real = float(input('\033[1;30mQuanto dinheiro você tem na carteira? R$\033[m'))

dolar = real / 4.32
euro = real / 4.73
iene = real / 0.039

print('Com \033[1;30m{}R$\033[m você pode comprar \033[1;30mU${:.2f}\033[m dólares, \033[1;30m{:.2f}\033[m euros e \033[1;30m{:.2f}\033[m ienes.'.format(real, dolar, euro, iene))







