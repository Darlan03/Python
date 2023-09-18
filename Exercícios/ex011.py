# Faça um programa que leia altura e alargura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessaria para pinta-la, sabendo que a cada litro de tinta pinta uma área de 2m**2.

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {:.1f} x {:.1f} e sua área é de {:.1f}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede você precisará de {}l de tinta'.format(tinta))