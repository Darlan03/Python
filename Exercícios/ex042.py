# Refaça o desafio 35, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

# ex035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
# formar um triângulo.

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a <= b + c and b <= a + c and c <= b + a:
    print('Os segmentos PODEM formar um triângulo.')
    if a == b and b == c:
        print('Esse triângulo possui todos os lados iguais então, ele é equilátero.')
    elif a != b and b != c and c != a:
        print('Esse triângulo possui todos os lados diferentes, então ele é escaleno.')
    else:
        print('Esse triângulo possui dois lados iguais, então ele é isósceles.')
else:
    print('Os segmentos NÃO podem formar um triângulo')