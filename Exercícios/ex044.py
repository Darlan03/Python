# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
# de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

pdt = float(input('Qual o valor da sua compra? R$ '))
print("""Esolha a forma de pegamento:
[1] À vista em dinheiro/cheque terá 10% de desconto!
[2] À vista no cartão terá 5% de desconto!
[3] Em até 2x no cartão s/ juros!
[4] 3x ou mais terá 20% de juros!""")
opção = int(input('Escolha a forma de pegamento: '))
if opção == 1:
    vista = pdt - ((pdt * 10)/100)
    print('Sua compra à vista sai a R${:.2f}'.format(vista))
elif opção == 2:
    crt5 = pdt - ((pdt * 5)/100)
    print('Sua compra com 5% de desconto sai a R${:.2f}'.format(crt5))
elif opção == 3:
    crt2x = pdt/2
    print('Sua compra foi parcelada em 2x de R${:.2f} s/ juros'.format(crt2x))
elif opção == 4:
    total = pdt + (pdt * 20 / 100)
    parc = int(input('Em quantas vezes deseja parcelar sua compra: '))
    total1 = total / parc
    print('Sua compra foi parcelada em {}x de R${:.2f}'.format(parc, total1))
else:
    print('Opção de pagamento inválida. Tente novente!')
