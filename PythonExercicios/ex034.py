salario = float(input('Digite o valor do salário do funcionário: R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava \033[31mR${:.2f}\033[m de salário passará a ganhar \033[34mR${:.2f}.'.format(salario, novo))


