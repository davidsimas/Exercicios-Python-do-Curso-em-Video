"""
Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares
e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

numero = [[], []]

for cont in range(1, 8):
    valor = int(input("Digite o {}º valor: ".format(cont)))

    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)

print("-=" * 30)
numero[0].sort()
numero[1].sort()
print("Os valores pares digitados foram: {}".format(numero[0]))
print("Os valores ímpares digitados foram: {}".format(numero[1]))