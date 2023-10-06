# Condições

# Comando if significa 'se' onde você é encaminhado para uma determinada tarefa.
# Comando else significa 'senão' onde se o 'se' for false o programa executará a linha de código else.
# Faça isso 'if', senão 'else' faça aquilo.

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

# Outra forma de escrever esse código é mais avançado, porém encurta o código
# print('Carro novo' if tempo <:3 else 'Carro velho')
# print('--FIM--')