"""
Faça um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um triângulo retângulo. Calcule e mostre o comprimento
da hipotenusa.
"""
from math import hypot


# Sem a importação do método MATH.
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))

hipot = ((co ** 2) + (ca ** 2)) ** (1 / 2)

print("A hipotenusa vai medir {:.2f}".format(hipot))

# Com a importação do método MATH.

hipo = hypot(co, ca)
print("A hipotenusa vai medir {:.2f}".format(hipo))