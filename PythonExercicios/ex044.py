preco = float(input('Qual o preço do produto? R$'))
pagamento = int(input('Qual a forma de pagamento?\n'
                      '\033[30m[1]\033[m Á vista \033[31mdinheiro/cheque;\033[m\n'
                      '\033[30m[2]\033[m Á vista no \033[34mcartão;\033[m\n'
                      '\033[30m[3]\033[m Até \033[32m2x no cartão;\033[m\n'
                      '\033[30m[4]\033[m \033[36m3x ou mais no cartão;\033[m\n'
                      ''))
if 0 < pagamento < 5:
    if pagamento == 1:
        pagamentoNovo = '\033[31má vista no dinheiro/cheque com desconto de 10%\033[m'
        novoValor = preco - (preco * (10/100))
    elif pagamento == 2:
        pagamentoNovo = '\033[34má vista no cartão com 5% de desconto\033[m'
        novoValor = preco - (preco * (5/100))
    elif pagamento == 3:
        pagamentoNovo = '\033[32maté 2x no cartão sem mudança de valor\033[m'
        novoValor = preco
    elif pagamento == 4:
        novoValor = preco + (preco * (20 / 100))
        parcelas = int(input('Em quantas parcelas deseja pagar? '))
        parcela = parcelas / novoValor
        pagamentoNovo = '\033[36m{}x no cartão COM JUROS\033[m'.format(parcelas)
        print('Sua compra será parcelada em {}x.'.format(parcelas))
    print('O valor do produto era \033[30m{}\033[m, com a forma de pagamento {}. O novo valor é \033[30m{}\033[m.'.format(preco, pagamentoNovo, novoValor))
else:
    print('Valor Inválido.')

