# Manipulação de texto

frase = 'Curso em Video Python'
var = frase[15:3:2]

# Dentro das chaves o primeiro número indica qual o início da contagem, o segundo indica onde vai parar
# O terceiro numero indica quantas casa vai pular

# Análise

# Função len mostra o comprimento da sequencia de caracteres
print(len(frase))

# Função count busca um determinado caracter dentro de uma sequencia e mostra quantos tem
frase.count('o')
frase.count('o', 0,13)

# Função find é encontrar em que posição aparece determinada sequencia de caracteres
frase.find('deo')

# Se procurar uma sequencia de caractere e o valor retornar -1 quer dizer que essa sequencia não existe onde esta procurando
frase.count('Android')

# Operador in ta perguntando se existe essa sequencia de caractere dentro da frase e retorna true ou false
var = 'Curso' in frase

# Transformação
# Função replace troca uma sequencia de caractere por outra, nesse exemplo ele trocou Python por Android
frase.replace('Python', 'Android')

# Método upper coloca todos os caracteres em maiusculo
frase.upper()

# Método lower troca os caracteres maiusculos por minusculos
frase.lower()

# Captalize deixa toda a string em minuscula e só deixa o primeiro caractere em maiusculo.
frase.capitalize()

# title deixa a primeira letra de cada palavra em maiuscula
frase.title()

# Função strip remove todos os espaços inuteis de uma string, menos o espaçamento entre palavras
frase.strip()

# Com a letra r do lado do strip indica que ira retirar os espaços da direita
frase.rstrip()

# Com a letra l do lado do strip indica que ira retirar os espaços da esquerda
frase.lstrip()

# Divisão
# Função split divide a string fazendo com que cada palavra tenha sua propria sequencia de caractere
# E coloca dentro de uma LISTA onde cada palavra indica um numero
frase.split()

# Junção
# Função join junta todos os elementos da frase
' '.join(frase)

# Função print() com 3""" no começo e mais """ no final seleciona o texto