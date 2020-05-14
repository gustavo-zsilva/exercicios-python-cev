nota1 = float(input('Digite sua primeira nota aqui: '))
nota2 = float(input('Digite sua segunda nota aqui: '))
media = (nota1 + nota2) / 2

if nota1 <= 10 and nota2 <=10:
    if media < 5:
        boletim = '\033[1;30;41mREPROVADO\033[m'
    elif media >= 5 and media <= 6.9:
        boletim = 'em \033[31mRECUPERAÇÃO\033[m'
    else:
        boletim = '\033[1;32mAPROVADO\033[m'
    print('Sua primeira nota foi {}, sua segunda {}, e sua média {:.1f}, portanto você está {}.'.format(nota1, nota2, media, boletim))
else:
    print('Valor Inválido.')