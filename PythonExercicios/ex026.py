frase = str(input('Digite uma frase: ')).strip().upper()

print('A letra "a" aparece {} vez(es) na frase. '.format(frase.count('A')))
print('A primeira letra "a" aparece na posição {}.'.format(frase.find('A')+1))
print('A última letra "a" aparece na posição {}.'.format(frase.rfind('A')))
