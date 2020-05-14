num1 = int(input('\033[1;4;31mDigite um número:\033[m '))
num2 = int(input('\033[4;35mDigite outro:\033[m '))
s = num1 + num2
print('A soma entre {}{}{} e {}{}{} é {}{}{}'.format('\033[36m', num1, '\033[m', '\033[34m',num2,'\033[m', '\033[4;31m', s,'\033[m'))
