# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

d = float(input('Quantos dias alugado? '))
km = float(input('Quantos km rodados? '))


km1 = km * 0.15
d1 = d * 60
c = km1 + d1

print('O carro alugado por {:.0f} dias.\nPercorreu {}km. \n'
      'Equivale a R${} pelos dias alugados e R${:.2f} pelos km rodados. \nPortanto o preço total do aluguel do carro sai a R${:.2f} '. format(d, km, d1, km1, c))