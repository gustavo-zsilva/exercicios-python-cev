from datetime import date
anoNascimento = int(input('Digite o ano que você nasceu: '))
genero = str(input('Você é homem ou mulher? (H ou M): ')).upper()
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if genero == 'H':
    if idade < 18:
        print('Ainda vai se alistar ao serviço militar daqui a {} anos.'.format(anoNascimento + 18 - anoAtual))
        print('Vai se alistar em {}.'.format(anoNascimento + 18))
    elif idade == 18:
        print('Está na hora do alistamento.')
    else:
        print('Já passou da hora do alistamento há {} anos.'.format(anoAtual - anoNascimento - 18))
        print('Ano do alistamento: {}.'.format(anoNascimento + 18))
else:
    print('Você não precisa fazer alistamento obrigatório.')
# anoNascimento - anoAtual == idade
# anoNascimento + 18 - anoAtual == quantos anos faltam
# anoAtual - anoNascimento - 18

