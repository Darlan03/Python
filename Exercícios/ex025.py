# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.

nom = str(input('Digite seu nome completo: ')).strip().title()
nom1 = 'Silva' in nom
print(nom1)
