# Faça um progrma que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
rad = radians(an)
sen = sin(rad)
cos = cos(rad)
tan = tan(rad)
print('O valor do seno é {:.2f} \nO valor do cosseno é {:.2f} \nO valor da tangente é {:.2f} '.format(sen, cos, tan))
