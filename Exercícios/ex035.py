# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('=-=-' * 6)
print('ANALISADOR DE TRIÂNGULOS')
print('=-=-' * 6)

print('Informe três segmento e direi se esses comprimentos podem formar um triângulo!')

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a <= b + c and b <= a + c and c <= b + a:
    print('Os segmentos PODEM formar um triângulo')
else:
    print('Os segmentos NÃO podem formar um triângulo')