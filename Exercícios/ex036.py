# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
# casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestaçao mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor do imóvel? R$'))
sal = float(input('Qual seu salário? R$'))
anos = float(input('Em quantos anos deseja pagar o imóvel? '))
mensal = (casa/anos)/12
print('O valor da mensalidade será de R${:.2f}'.format(mensal))
if mensal > (sal*30)/100:
    print('Seu empréstimo foi negado por exceder 30% do seu salário. ')
else:
    print('Parabéns!\nSeu empréstimo foi liberado!!!')

