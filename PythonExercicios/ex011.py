alt = float(input('\033[30mQual a altura da parede? m'))
lar = float(input('Qual a largura da parede? m\033[m'))

area = alt * lar
tin = area / 2

print('\033[1;31mA dimensão de sua parede é de {} x {} e sua área é de {:.3f}m quadrados,'.format(alt, lar, area), end = ' portanto ')
print('precisará de {:.2f} litros de tinta. '.format(tin))