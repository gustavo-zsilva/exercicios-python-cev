nome = str(input('Qual seu nome completo? ')).strip()
n = nome.upper().split()

print('O seu nome tem Silva? {}'.format('SILVA' in n))
