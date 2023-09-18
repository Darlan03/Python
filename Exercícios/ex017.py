# Faça um programa que leia o comprimento do catetro oposto e do cateto adjacente de um triangulo relantgulo,
# Calcule e mostre o comprimento desse angulo

from math import hypot
co = float(input('Qual o cateto oposto: '))
ca = float(input('Qual o cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f} '.format(hi))