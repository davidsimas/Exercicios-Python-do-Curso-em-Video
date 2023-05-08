"""
Crie um programa que leia o nome de uma pessoa
e diga se ela tem "SILVA" no nome.
"""


nome = str(input("Qual é seu nome completo? ")).strip()

# Usando um operador do Python "IN".
print("Seu nome tem Silva? {}".format("SILVA" in nome.upper()))