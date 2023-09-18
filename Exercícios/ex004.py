# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

n = input('Digite um valor: ')
print('O tipo primitivo desse valor é ', type(n))

print('Só tem espaços? ',n.isspace())
# isspace é para saber se só tem espaços.

print('É um número? ',n.isnumeric())
# isnumeric é para saber se é numerico.

print('É alfanumerico? ',n.isalnum())
# isalnum é para saber se é alfanumerico.

print('Esta em maiuscula? ',n.isupper())
# isupper é para saber se o texto está em maiusculo.

print('Está em minusculo? ',n.islower())
# islower é para saber se o texto está em minusculo.

print('Esta capitalizada? ',n.isalnum())
# istitle á para saber se o texto está com letras maiusculas e minusculas.

print('O valor {} é alfanumerico? '.format(n), n.isalnum())
# .format é para substituir o valor que está dentro das chaves {}.