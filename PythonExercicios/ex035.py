print('''\033[1;36m--=--=--=--=--=--=--=--=--=--=--=--
   \033[1;34mANALISADOR DE TRIÂNGULOS
\033[1;36m--=--=--=--=--=--=--=--=--=--=--=--\033[m ''')

seg1 = float(input('Primeiro Segmento: '))
seg2 = float(input('Segundo Segmento: '))
seg3 = float(input('Terceiro Segmento: '))
if seg1 + seg2 > seg3 and seg3 + seg2 > seg1 and seg1 + seg3 > seg2:
    resp = '\033[36mPÔDE\033[m'
else:
    resp = '\033[31mNÃO PÔDE\033[m'
print('O triângulo acima {} ser formado!'.format(resp))
