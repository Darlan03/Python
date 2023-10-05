# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.

cid = str(input('Digite o nome da sua cidade: '))
cid0 = cid.strip()
cid1 = cid0.capitalize()
cid2 = 'Santo' in cid1
print(cid2)