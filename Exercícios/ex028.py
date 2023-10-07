# Escreva um programa que faça o pc 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo pc.
# O programa deverá escrever na tela se o usuário vendeu ou perdeu.

from random import randint
from time import sleep
pc = randint(0, 5)  # Faz o pc 'pensar'
print('-=-' * 18)
print('Vou pensar em um número entre 0 e 5, tente adivinhar!')
print('-=-' * 18)
jogador = int(input('Em que número pensei? '))  # jogador tenta adivinhar
print('Processando...')
sleep(1)
if jogador == pc:
    print('Parabéns, você venceu!!!')
else:
    print('Ganhei, pensei no número {} e não {}!'.format(pc, jogador))
