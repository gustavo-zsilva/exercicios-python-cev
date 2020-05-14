dis = float(input('Qual a distância da viagem? '))
preco = dis * 0.50 if dis <= 200 else dis * 0.45
print('E o preço da sua passagem será R${}.'.format(preco))
'''if dis <= 200:
    print('O preço da passagem é {:.2f}R$.'.format(dis * 0.50))
else:
    print('O preço da passagem será {:.2f}R$.'.format(dis * 0.45))'''
