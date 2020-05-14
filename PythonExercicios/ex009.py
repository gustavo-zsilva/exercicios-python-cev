cores=  {'limpo':'\033[m', 'branco':'\033[30m', 'azul':'\033[34m', 'vermelho':'\033[31m', 'ciano':'\033[36m', 'roxo':'\033[35m'}

num = int(input('Digite um número qualquer: '))

num1 = num * 0
num2 = num * 1
num3 = num * 2
num4 = num * 3
num5 = num * 4
num6 = num * 5
num7 = num * 6
num8 = num * 7
num9 = num * 8
num10 = num * 9
num11 = num * 10

print('-' * 12)
print(
    " {} x 0 = {:2} \n {} x 1 = {:2} \n {} x 2 = {} \n {} x 3 = {} \n {} x 4 = {} \n {} x 5 = {} \n {} x 6 = {} \n {} x 7 = {} \n {} x 8 = {} \n {} x 9 = {} \n {} x 10 = {}".format(num, num1, num, num2, num, num3, num, num4, num, num5, num, num6, num, num7, num, num8, num, num9, num, num10, num, num11))
print('\033[1;30m-' * 12)
# ou

print('{}{} x {:2} = {}'.format(cores['vermelho'] ,num, 1, num*1))
print('{}{} x {:2} = {}'.format(cores['azul'] ,num, 2, num*2))
print('{}{} x {:2} = {}'.format(cores['branco'] ,num, 3, num*3))
print('{}{} x {:2} = {}'.format(cores['ciano'] ,num, 4, num*4))
print('{}{} x {:2} = {}'.format(cores['roxo'] ,num, 5, num*5))
print('{}{} x {:2} = {}'.format(cores['vermelho'] ,num, 6, num*6))
print('{}{} x {:2} = {}'.format(cores['azul'] ,num, 7, num*7))
print('{}{} x {:2} = {}'.format(cores['branco'] ,num, 8, num*8))
print('{}{} x {:2} = {}'.format(cores['ciano'] ,num, 9, num*9))
print('{}{} x {:2} = {}'.format(cores['roxo'] ,num, 10, num*10))
print('\033[1;30m-' * 12)

