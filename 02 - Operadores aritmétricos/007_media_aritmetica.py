"""
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua 
média.
"""


numero1 = float(input("Digite a primeira nota do aluno: "))
numero2 = float(input("Digite a segunda nota do aluno: "))

media = (numero1 + numero2) / 2
# Depois do ponto flutuante coloque apenas 2 digitos. 
print("A média entre {:.2f} e {:.2f} é igual a {:.2f}".format(numero1, numero2, media))