# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

preco = float(input('Qual o preço do produto? R$'))
print('O produto que custava R${}'.format(preco))
desc = preco - (preco * 5 / 100)

print('Com 5% de desconto vai custar R${:.2f}'.format(desc))