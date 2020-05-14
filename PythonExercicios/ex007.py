
nota1 = float(input('Digite sua primeira nota: '))
if nota1 > 10:
    print('\033[31mEssa nota não existe.\033[m')
else:
    nota2 = float(input('Digite sua segunda nota: '))

    if nota2 > 10:
        print('\033[1;31mEssa nota não existe.\033[m')

    elif nota1 <= 10 and nota2 <= 10:
        med = (nota1 + nota2) / 2
        print('A sua \033[36mprimeira nota foi {},\033[m \033[1;35ma sua segunda {},\033[m portanto sua \033[1;33mmédia aritmética é {:.1f}\033[m'.format(nota1, nota2, med))

print('{}Programa encerrado.'.format('\033[1;31m'))


