from math import radians, sin, cos, tan
an = float(input('Digite o ângulo: '))

cos = cos(radians(an))
sen = sin(radians(an))
tan = tan(radians(an))

print('O SENO de {} graus é {:.2f} \\ O COSSENO é {:.2f} \\ A TANGENTE é {:.2f}'.format(an, sen, cos, tan))



