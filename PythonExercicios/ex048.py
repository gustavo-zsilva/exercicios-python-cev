contador = 0
soma = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n
        contador += 1

print('A soma dos {} valores obtidos é {}.'.format(contador, soma))
