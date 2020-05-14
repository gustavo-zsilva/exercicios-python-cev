cores = {'vermelhoN':'\033[1;31m'}
dia = int(input('\033[1;31mPor quantos dias o carro foi alugado? '))
km = float(input('\033[1;31mQuanto km rodados com o carro? '))

total = (60 * dia) + (0.15 * km)
#custokm = km * 0.15
#total = custod + custokm

print('\033[1;30mO total a pagar é \033[1;36mR${:.2f}'.format(total))
