# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
# de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

pdt = float(input('Qual o valor do produto? R$'))
print("""Esolha a forma de pegamento:
[1] À vista em dinheiro ou cheque terá 10% de desconto!
[2] À vista no cartão terá 5% de desconto!
[3] Em até 2x no cartão s/ juros!
[4] 3x ou mais terá 20% de juros!""")
opção = int(input('Escolha a forma de pegamento: '))
if opção == 1:
    vista = pdt - ((pdt * 10)/100)
    print('O produto à vista sai a R${:.2f}'.format(vista))
elif opção == 2:
    crt5 = pdt - ((pdt * 5)/100)
    print('O produto com 5% de desconto sai a R${:.2f}'.format(crt5))
elif opção == 3:
    crt2x = pdt/2
    print('O produto em 2x s/ juros sai a R${:.2f} na primeira parcela e R${:.2f} na segunda parcela'.format(crt2x, crt2x))
elif opção == 4
    crt3x


