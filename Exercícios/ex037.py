# Escreva um programa que leia um número e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input('Digite um número: '))
print("""Escolha a base de conversão:
[1] para Binário
[2] para Octal
[3] para Hexadecimal""")
opção = int(input('Escolha sua opção: '))
if opção == 1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, Tente novamente!')
