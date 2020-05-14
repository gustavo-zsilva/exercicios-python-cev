from random import randint
from time import sleep
randint = randint(0,5)
chute = int(input('Vou pensar em um número de 0 a 5, tente adivinhar: '))
print('PROCESSANDO...')
sleep(3)
if chute == randint:
    print('Parabéns, você acertou!')
else:
    print('Você errou!')
    print('Eu pensei no número {} e não {}! '.format(randint, chute))
print('Foi bom jogar com você!')
