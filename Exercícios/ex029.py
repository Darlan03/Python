# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

from time import sleep
from random import randint
velocidade = randint(79, 90)
print('---' *12)
print('CUIDADO, RADAR À FRENTE!\nLimite de velocidade 80km/h')
print('---' *12)
print('Verificando velocidade do veículo...')
print('---' *12)
sleep(3)
print('A velocidade registrada foi de {}Km/h'.format(velocidade))
if velocidade > 80:
    multa = (velocidade-80) * 7
    print('Excedeu o limite de velocidade de 80km/h\nVocê foi multado em R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! \nDirija com segurança!')
