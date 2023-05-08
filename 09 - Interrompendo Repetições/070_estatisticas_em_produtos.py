"""
Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 
"""


total = 0
total_mil = 0
menor = 0
cont = 0
barato = ""

while True:
    produto = str(input("Nome do Produto: "))
    preco = float(input("Preço: R$ "))

    cont += 1
    total += preco
    if preco > 1000:
        total_mil += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto


    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break

print("{:-^40}".format(" Fim do Programa "))
print("O total da compra foi {:.2f}".format(total))
print("O produto mais barato foi {} que custa R${:.2f}".format(barato, menor))