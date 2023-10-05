# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.

cid = str(input('Digite o nome da sua cidade: ')).strip().capitalize()
cid1 = 'Santo' in cid
print(cid1)