"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em
uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""


temp = []
principal = []
maior = 0
menor = 0

while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))

    if len(principal) == 0:
        maior = temp[1]
        menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    # Criar uma cópia da lista temp para a principal
    principal.append(temp[:])
    # Limpar a lista temp
    temp.clear()

    resp = str(input("Quer continuar? [S/N]"))

    if resp in "Nn":
        break

print("-= * 30")
# print("Os dados foram {}".format(principal))
print("Ao todo, você cadastrou {} pessoas.".format(len(principal)))
print("O maior peso foi de {}KG. Peso de ".format(maior), end="")
for pessoa in principal:
    if pessoa[1] == maior:
        print(pessoa[0], end=" ")
print()
print("O menor peso foi de {}KG. Peso de ".format(menor), end="")
for pessoa in principal:
    if pessoa[1] == menor:
        print(pessoa[0], end=" ")