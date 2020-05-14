num1 = int(input('Digite um número: '))
dob = num1 * 2
trip = num1 * 3
raiz = num1 ** (1/2)
print('O dobro de \033[31m{}\033[m é \033[35m{}\033[m, o seu triplo é \033[34m{}\033[m e sua raíz quadrada é \033[1;36m{:.2f}\033[m.'.format(num1, dob, trip, raiz))

