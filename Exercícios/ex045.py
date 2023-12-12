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
if pc == 0:
    if j1 == 0:
        print('Deu empate!')
    elif j1 == 1:
        print('Você ganhou!')
    elif j1 == 2:
        print('PC ganhou!')
    else:
        print('Jogada inválida. Tente novamente!')
elif pc == 1:
    if j1 == 0:
        print('PC ganhou!')
    elif j1 == 1:
        print('Deu empate!')
    elif j1 == 2:
        print('Você ganhou!')
    else:
        print('Jogada inválida. Tente novamente!')
elif pc == 2:
    if j1 == 0:
        print('Você ganhou!')
    elif j1 == 1:
        print('PC ganhou!')
    elif j1 == 2:
        print('Deu empate!')
    else:
        print('Jogada inválida. Tente novamente!')
else:
    print('Jogada inválida. Tente novamente!')
