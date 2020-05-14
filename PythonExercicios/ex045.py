from random import choice
from time import sleep

palpite = str(input('Digite o valor que deseja jogar: (pedra, papel, tesoura) ')).upper()
lista = ['PEDRA','PAPEL','TESOURA']
cpuChoice = choice(lista)

if palpite == 'TESOURA' or palpite == 'PEDRA' or palpite == 'PAPEL':

    print('JO')
    sleep(0.8)
    print('KEN')
    sleep(0.8)
    print('PO!')
    sleep(0.5)


    # EMPATE
    if palpite == cpuChoice:

        round = '\033[1;30m--=--EMPATE--=--'

    # CPU GANHOU
    elif palpite == 'PEDRA' and cpuChoice == 'PAPEL':
        round = 'CPU GANHOU! Você escolheu \033[1mPEDRA\033[m e CPU escolheu \033[1;30mPAPEL.\033[m'
    elif palpite == 'PAPEL' and cpuChoice == 'TESOURA':
        round = 'CPU GANHOU! Você escolheu \033[1;30mPAPEL\033[m e CPU escolheu \033[31mTESOURA.\033[m'
    elif palpite == 'TESOURA' and cpuChoice == 'PEDRA':
        round = 'CPU GANHOU! Você escolheu \033[31mTESOURA\033[m e CPU escolheu \033[1mPEDRA.\033[m'

    # VOCÊ GANHOU
    elif palpite == 'PAPEL' and cpuChoice == 'PEDRA':
        round = 'VOCÊ GANHOU! Você escolheu \033[1;30mPAPEL\033[m e CPU escolheu \033[1mPEDRA\033[m'
    elif palpite == 'PEDRA' and cpuChoice == 'TESOURA':
        round = 'VOCÊ GANHOU! Você escolheu \033[1mPEDRA\033[m e CPU escolheu \033[31mTESOURA.\033[m'
    elif palpite == 'TESOURA' and cpuChoice == 'PAPEL':
        round = 'VOCÊ GANHOU! Você escolheu \033[31mTESOURA\033[m e CPU escolheu \033[1;30mPAPEL.\033[m'


    # Checando valor de round para definir tamanho das linhas
    if palpite == cpuChoice:
        print('-=' * 10)
        print(round)
        print('-=' * 10)
    else:
        print('-=' * 30)
        print(round)
        print('-=' * 30)

else:
    print('\033[1;31mValor Inválido.')

