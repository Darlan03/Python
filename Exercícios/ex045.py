# Crie um programa que faça o pc jogar jokenpô com você

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('VAMOS JOGAR JOKENPÔ')
j1 = int(input("""[0] Pedra
[1] Papel
[2] Tesoura
Faça sua jogada: """))
print('-=' * 10)
print('Você escolheu {}'.format(itens[j1]))
print('PC escolheu {}'.format(itens[pc]))
print('-=' * 10)

