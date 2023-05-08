"""
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

valores = []

while True:
    valores.append(int(input("Digite um valor: ")))
    resp = str(input("Deseja continuar? [S/N]"))
    if resp in "Nn":
        break

# Quantos números foram digitados.
print("-=" * 30)
print("Você digitou {} elementos.".format(len(valores)))

# A lista de valores, ordenada de forma decrescente.
print("-=" * 30)
valores.sort(reverse=True)
print("Os valores em ordem decrescente são {}".format(valores))

# Se o valor 5 foi digitado e está ou não na lista.
print("-=" * 30)
if 5 in valores:
    print("O valor 5 faz parte da lista.")
else:
    print("O valor 5 não foi encontrado na lista.")