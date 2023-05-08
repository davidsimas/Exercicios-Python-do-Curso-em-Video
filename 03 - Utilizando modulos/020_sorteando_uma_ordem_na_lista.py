"""
O mesmo professor do desafio 019 quer sortear a ordem de apresentação de
trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
e mostre a ordem sorteada.
"""
from random import shuffle


nome1 = str(input("Primero aluno: "))
nome2 = str(input("Segundo aluno: "))
nome3 = str(input("Terceiro aluno: "))
nome4 = str(input("Quarto aluno: "))

# Lista de alunos
lista = [nome1, nome2, nome3, nome4]

ordem = shuffle(lista)

print("A ordem de apresentação será ")
print(lista)