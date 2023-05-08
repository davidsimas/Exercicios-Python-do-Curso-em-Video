"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""
from math import factorial


num = int(input("Digite um número para calcular seu Fatorial: "))
# Utilizando Moodulo.
# fatorial = factorial(num)
cont = num
fatorial = 1

print("Calculando {}! = ".format(num), end = "")
while cont > 0:
    print("{}".format(cont), end = "")
    print(" x " if cont > 1 else " = ", end = "")
    fatorial *= cont
    cont -= 1

print("{}".format(fatorial))