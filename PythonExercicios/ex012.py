preço = float(input('Qual o preço do item? R$'))

novopreço = preço - (preço * 5 / 100)
print('\033[1;36m-=-' * 27)
print('O produto que custava \033[36m{:.2f}\033[m passará a custar, com o desconto de \033[35m5%, {:.2f}.'.format(preço, novopreço))
print('\033[1;36m-=-' * 27)



