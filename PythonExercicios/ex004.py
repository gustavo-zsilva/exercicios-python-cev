# Dicionário de cores:
cores = {'limpo':'\033[m', 'azul':'\033[34m', 'vermelho':'\033[31m', 'verde':'\033[32m', 'branco':'\033[30m', 'amarelo':'\033[33m', 'roxo':'\033[35m'}

n = input('Digite algo: ')

# Verificar o tipo da variável
print(type(n))

# Primeiro modo de resolver em várias linhas:

# print('numerico =', n.isnumeric())
# print('alfabético =', n.isalpha())
# print('alfanumérico =', n.isalnum())
# print('decimal =', n.isdecimal())
# print('ascii = (ainda não resolvido)')
# print('letras minusculas =', n.islower())
# print('letras maíusculas =', n.isupper())
# print('espaço =', n.isspace())
# print('identificador =', n.isidentifier())
# print('imprimível =', n.isprintable())
# print('dígito =', n.isdigit())
# print('título =', n.istitle())

# Segundo jeito de resolver o exercício em apenas 3 linhas:

is1 = n.isnumeric()
is2 = n.isalpha()
is3 = n.isalnum()
is4 = n.isdecimal()
is5 = n.islower()
is6 = n.isupper()
is7 = n.isspace()
is8 = n.isidentifier()
is9 = n.isprintable
is10 = n.isdigit()
is11 = n.istitle()

print("{}numerico = {}. {}alfa = {}. {}alfanum = {}. {}decimal = {}. {}ascii = (). {}lower = {}."
      "upper = {}. space = {}. identifier = {}. printable = {}. digit = {}. title = {}".format(cores['azul'], is1, cores['vermelho'] ,is2,  cores['verde'] ,is3, cores['branco'],is4,
                   cores['amarelo'],is5, cores['roxo'] ,is6, cores['azul'],is7, cores['vermelho'] ,is8, cores['verde'] ,is9, cores['branco'] ,is10, cores['amarelo'] ,is11))
