from random import randint

random_num = randint(0,10)
tentativas = 0
print('Pensei em um número. Tente adivinhá-lo.')
palpite = int(input('Digite seu palpite: '))

while palpite != random_num:

    if palpite > random_num:
        print('Tente um número menor.')
        tentativas += 1
    elif palpite < random_num:
        print('Tente um número maior.')
        tentativas += 1
    palpite = int(input('Digite seu palpite: '))

print(f'Você acertou, era o número {random_num}! O número de tentativas foi {tentativas}.')
