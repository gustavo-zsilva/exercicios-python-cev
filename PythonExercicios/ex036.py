casa = float(input('Qual é o valor da casa? '))
salario = float(input('Quanto é seu salário? '))
anos = int(input('Em quantos anos você vai pagar? '))

percent = salario * (30/100)
prestacao = casa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestacao))
if prestacao <= percent:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')

