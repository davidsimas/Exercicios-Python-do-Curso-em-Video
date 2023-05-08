"""
Faça um programa que leia um número Inteiro qualquer e mostre 
na tela a sua tabuada.
"""


num = int(input("Digite um número para ver sua tabuada: "))

print("-" * 12)
for indice in range(1, 11):
    print("{} x {:2} = {}".format(num, indice, (num * indice)))
print("-" * 12)