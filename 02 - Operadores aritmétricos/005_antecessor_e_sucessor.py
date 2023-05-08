"""
Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
"""


num = int(input("Digite um número: "))

ant = num - 1
suc = num + 1

print("Analisando o númeor {}, seu antecessor é {} e o sucessor é {}".format(num, ant, suc))

# Ou de forma direta
print("Analisando o númeor {}, seu antecessor é {} e o sucessor é {}".format(num, (num - 1), (num + 1)))