media = 0
mais_velho = ' '
idade_pessoa = 0
total_mulheres = 0
idade_mulheres = 0

for pessoa in range(1,5):
    print('----- PESSOA {} -----'.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    if pessoa == 1 and sexo == 'M':
        mais_velho = nome
        idade_pessoa = idade

    if sexo == 'M' and idade > idade_pessoa:
        mais_velho = nome
        idade_pessoa = idade

    if sexo == 'F' and idade < 20:
        total_mulheres += 1

    media += idade

print('A média de idade do grupo é {:.1f}.'.format(media / 4))
print('O homem mais velho do grupo tem {} anos e se chama {}.'.format(idade_pessoa, mais_velho.capitalize()))
print('O total de mulheres com menos de 20 anos é {}.'.format(total_mulheres))
