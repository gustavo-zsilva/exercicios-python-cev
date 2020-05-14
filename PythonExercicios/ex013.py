sal = float(input('\033[1;31mSalário do funcionário: R$ '))
sal2 = sal + (sal * (15/100))

print('\033[36mO funcionário que ganhava R${:.2f} \033[1;35mcom 15% de aumento passará a ganhar R${:.2f}.'.format(sal, sal2))
