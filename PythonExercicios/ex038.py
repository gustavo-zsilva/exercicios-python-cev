num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
maior = num1

if num1 > num2:
    print('O primeiro valor,{},é maior.'.format(maior))
elif num2 > num1:
    maior = num2
    print('O segundo valor ,{},é maior.'.format(maior))
else:
    print('Os dois valores são iguais.')
