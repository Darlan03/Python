# Um professor quer soretear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome do escolhido.

import random
a1 = str(input('Nome do aluno 1: '))
a2 = str(input('Nome do aluno 2: '))
a3 = str(input('Nome do aluno 3: '))
a4 = str(input('Nome do aluno 4: '))
lista = [a1, a2, a3, a4]
escolhido = random.shuffle(lista)
print('O aluno escolhido foi {} '.format(escolhido))
