#Faça um programa que leia um número real qualquer pelo teclado e mostre sua porção inteira
#Ex: Digite um numero: 6.127
#O numero 6.127 te, a parte inteira 6.

from math import trunc
num = float(input('Digite um número: '))
print('O número escolhido foi {} e sua porção inteira é {}.'.format(num, trunc(num)))

