vel = float(input('Qual a velocidade do carro? (km/h): '))

if vel > 80:
    print('\033[31mVocê foi multado em {:.2f} reais por exceder a velocidade em {} km.\033[m'.format((vel - 80) * 7, vel - 80))

else:
    print('\033[36mVocê não foi multado.\033[36m')
    