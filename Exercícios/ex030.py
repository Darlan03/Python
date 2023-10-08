# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

num = int(input('Digite um número e direi se ele é ímpar ou par: '))
resto = num % 2
if resto == 1:
    print('Este número é ímpar!')
else:
    print('Este número é par!')
