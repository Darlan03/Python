# Faça um programa que leia três números e mostre qual é maior e qual é menor.

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
maior = a
if b > c and b > a:
    maior = b
if c > b and c > a:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
