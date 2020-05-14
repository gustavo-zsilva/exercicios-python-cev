from datetime import date
anoNascimento = int(input('Digite o ano de nascimento do atleta: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

print('O atleta tem {} anos.'.format(idade))
if anoNascimento <= anoAtual:
    if idade <= 9:
        categoria = 'MIRIM'
    elif idade <= 14:
        categoria = 'INFANTIL'
    elif idade <= 19:
        categoria = 'JÚNIOR'
    elif idade <= 25:
        categoria = 'SÊNIOR'
    else:
        categoria = 'MASTER'
    print('A categoria do atleta é {}.'.format(categoria))
else:
    print('Ano Inválido')
