# Crie um programa que leia o nome de uma pessoa e mostre:
# O nome com todas as letras maiusculas.
# O nome com minusculas.
# Quantas letras ao total sem considerar espaços.
# quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('Em letras maiúsculas é {}:'.format(nome.upper()))
print('Em letras minúsculas é {}:'.format(nome.lower()))
print('Tem um total de {} letras.'.format(len(nome) - nome.count(' ')))
print('E o primeiro nome tem {} letras'.format(nome.find(' ')))
