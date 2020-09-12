sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('\033[31mValor Inválido. Digite seu sexo novamente \033[36m[M\033[35m/F]:\033[m ')).strip().upper()[0]

print(f'Sexo {sexo} informado. Cadastro Concluído.')