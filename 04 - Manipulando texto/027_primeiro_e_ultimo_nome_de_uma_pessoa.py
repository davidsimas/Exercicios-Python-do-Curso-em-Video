"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e o último nome separadamente.

Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.
"""


nome = str(input("Digite seu nome completo: ")).strip()

# Pega uma String e transforma em uma lista.
nome_lista = nome.split()

print("Seu primeiro nome é {}".format(nome_lista[0]))
print("Seu último nome é {}".format(nome_lista[len(nome_lista) - 1]))