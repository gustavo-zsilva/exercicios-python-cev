seg1 = float(input('Digite um segmento de reta: '))
seg2 = float(input('Digite outro segmento de reta: '))
seg3 = float(input('Digite outro segmento de reta: '))

if seg1 + seg2 > seg3 and seg2 + seg3 > seg1 and seg1 + seg3 > seg2:
    if seg1 == seg2 == seg3:
        print('O triângulo pode ser formado e é \033[31mEQUILÁTERO.')
    elif seg1 == seg2 != seg3 or seg2 == seg3 != seg1 or seg1 == seg3 != seg2:
        print('O triângulo pode ser formado e é \033[36mISÓSCELES.')
    else:
        print('O triângulo pode ser formado e é \033[34mESCALENO.')
else:
    print('O triângulo \033[31mnão pode\033[m ser formado.')
