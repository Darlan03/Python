# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# primeiro = Ana
# útimo = Souza
import ntpath

nome = str(input('Digite seu nome completo: ')).strip()
nom = nome.split()
print('Seu primeiro nome é {}'.format(nom[0]))
print('Seu último nome é {}'.format(nom[len(nom)-1]))
