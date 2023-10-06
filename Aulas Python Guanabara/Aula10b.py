# nome = str(input('Qual seu nome? ')).strip().capitalize()
# if nome == 'Darlan':
#    print('Que nome lindo')
# else:
#    print('Seu nome é tão normal!')
# print('Bom dia, {}!'.format(nome))

# print('Que nome lind0' if nome == 'Darlan' else 'Seu nome é tão normal!')
# print('Bom dia, {}!\n--FIM--'.format(nome))

n1 = float(input('Digite uma nota de 0 a 10: '))
n2 = float(input('Digite outra nota de 0 a 10: '))
m = (n1+n2)/2
if m >= 7:
    print('Sua nota é {}\nParabéns, você está aprovado!'.format(m))
else:
    print('Sua nota é {}\nPoxa que pena, você foi reprovado!'.format(m))
print('Até o próximo semestre!')
