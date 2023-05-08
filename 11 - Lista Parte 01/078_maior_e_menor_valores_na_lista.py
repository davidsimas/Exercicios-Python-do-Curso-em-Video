"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas
respectivas posições na lista. 
"""


lista_num = []
maior = 0
menor = 0

for cont in range(0, 5):
    lista_num.append(int(input("Digite um valor para a Posição {}: ".format(cont))))

    if cont == 0:
        maior = menor = lista_num[cont]
    else:
        if lista_num[cont] > maior:
            maior = lista_num[cont]
        if lista_num[cont] < menor:
            menor = lista_num[cont]

print("=-" * 30)
print("Você digitou os valores {}".format(lista_num))
print("O maior valor digita foi {} nas posições ".format(maior), end = "")
for i, v in enumerate(lista_num):
    if v == maior:
        print("{}...".format(i), end = "")
print()
print("O menor valor digita foi {} nas posições ".format(menor), end = "")
for i, v in enumerate(lista_num):
    if v == menor:
        print("{}...".format(i), end = "")
print()