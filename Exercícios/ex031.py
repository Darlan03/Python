# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50
# por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.

vig = int(input('Qual a distância em km da sua viagem? '))
if vig <= 200:
    preco = vig * 0.50
else:
    preco = vig * 0.45
print('Sua viagem custará R${:.2f}'.format(preco))
