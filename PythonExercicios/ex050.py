contador = 0
soma = 0
for n in range(1, 7):
    num = int(input('Digite o {}º número: '.format(n)))
    if num % 2 == 0:
        soma += num
        contador += 1
if contador > 1:
    print('A soma dos números pares ({}) é {}.'.format(contador, soma))
if contador == 1:
    print('Você informou apenas 1 número par, "{}".'.format(soma))
else:
    print('Não há números pares.')

