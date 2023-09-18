# Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dolares ela pode comprar
# considerando o dolar US$1,00=R$3,27
r = float(input('Quantos reais você tem na carteira? '))
print('Com {:.0f}R$ você pode comprar {:.2f}US$ '.format(r, r/3.27))