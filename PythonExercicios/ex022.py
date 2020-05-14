nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em minusculas é {}.'.format(nome.lower()))
print('Seu nome em maiusculas é {}.'.format(nome.upper()))
print('Seu nome tem ao todo {} letras. '.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(nome.split()[0], len(nome.split()[0])))
