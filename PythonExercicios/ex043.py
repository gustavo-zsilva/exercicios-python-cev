peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    categoria = 'Abaixo do peso'
elif 18.5 <= imc < 25:
    categoria = 'Peso Ideal'
elif 25 <= imc < 30:
    categoria = 'Sobrepeso'
elif 30 <= imc < 40:
    categoria = 'Obesidade'
else:
    categoria = 'Obesidade Mórbida'
print('Seu IMC é {:.2f} e sua categoria é {}.'.format(imc, categoria))

