nome = str(input('Digite seu nome: ')).upper().strip()
nome = ''.join(nome.split())

nomerev = nome[::-1]

'''contador = 0

for c in range(len(nome), 0, -1):

    print(nome[contador], end='')
    contador += 1'''

print(f'O reverso de {nome} é {nomerev}.')

if nome == nomerev:
    print('O nome É um PALÍNDROMO.')
else:
    print('O nome NÃO É um PALÍNDROMO.')
