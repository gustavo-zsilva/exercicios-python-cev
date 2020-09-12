num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

print('O que deseja fazer com estes números? ')
opcao = '''\033[36m[ 1 ] Somar
\033[34m[ 2 ] Multiplicar
\033[32m[ 3 ] Maior
\033[35m[ 4 ] Novos Números
\033[1;31m[ 5 ] Sair do programa
\033[m
'''
print(opcao)
menu = int(input('Opção: '))

while menu != 5:
    if menu == 1:
        resultado = num1 + num2
        print(f'A soma de {num1} e {num2} é {resultado}.')
    if menu == 2:
        resultado = num1 * num2
        print(f'O produto de {num1} com {num2} é {resultado}.')
    if menu == 3:
        if num1 > num2:
            resultado = num1
            print(f'O maior entre {num1} e {num2} é {resultado}.')
        elif num2 > num1:
            resultado = num2
            print(f'O maior entre {num1} e {num2} é {resultado}.')
    if menu == 4:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))

    print('')

    print(opcao)
    menu = int(input('Opção: '))

print('\033[1;41m Programa terminado. \033[m')
