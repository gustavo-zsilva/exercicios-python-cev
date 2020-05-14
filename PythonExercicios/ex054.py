from datetime import date

data = date.today().year
maiores = 0
menores = 0

for c in range(1,8):
    ano = int(input('Digite o ano que a {}ª pessoa nasceu: '.format(c)))

    if data - ano >= 18:
        maiores += 1
    else:
        menores += 1
    if ano >= data:
        print('\033[31mValor Inválido.')
        break

else:
    if maiores == 0:
        valor = 'Não temos maiores de idade, então temos 7 menores.'
    elif menores == 0:
        valor = 'Não temos menores de idade, então temos 7 maiores.'
    elif maiores == 1:
        valor = 'Temos 1 maior de idade e 6 menores.'
    elif menores == 1:
        valor = 'Temos 1 menor de idade e 6 maiores.'
    else:
        valor = 'Temos {} maiores e {} menores de idade.'.format(maiores, menores)
    print(valor)

