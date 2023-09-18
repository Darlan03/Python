# Escreva um programa que leia um valor em metros e o exiba em centimetros e milimetros.

n1 = float(input('Uma distância em metros: '))
cm = n1*100
mm = n1*1000
print('A medida de {}m em centimetros corresponde a {:.0f}cm \nE em milimetros corresponde a {:.0f}mm '.format(n1, cm, mm))