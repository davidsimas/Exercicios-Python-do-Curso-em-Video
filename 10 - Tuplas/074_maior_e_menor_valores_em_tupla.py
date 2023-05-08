"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma
tupla. Depois disso, mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla.
"""
from random import randint


numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
          randint(1, 10), randint(1, 10))

print("Os valores sorteados foram: ", end = "")
for numero in numeros:
    print("{}".format(numero), end = " ")

# Menor valor
print("\nO menor valor sorteado foi {}".format(min(numeros)))

# Maior valor
print("O maior valor sorteado foi {}".format(max(numeros)))
