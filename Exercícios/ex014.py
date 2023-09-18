# Escreva um programa que converta uma temperatura digitada em °C e converta para °F

a = float(input('Digite uma temperatura em °C: '))
f = (a * 1.8) + 32
print('{} °C equivale a {} °F'.format(a, f))