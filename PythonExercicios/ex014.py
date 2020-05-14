celsius = float(input('Digite a temperatura em graus Celsius: '))
fahrenheit = 9 * celsius / 5 + 32

if celsius <= 10:
    print('\033[1;30mA temperatura em fahrenheit é {:.1f}.'.format(fahrenheit))
else:
    print('\033[1;31mA temperatura em fahrenheit é {:.1f}.'.format(fahrenheit))

