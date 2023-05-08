"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai mostrar a soma entre todos os valores
pares sorteados pela função anterior.
"""
from time import sleep
from random import randint


def sorteia(lista):
    print("Sorteando 10 valores da lista: ")
    for cont in range(0, 10):
        numero = randint(1, 100)
        lista.append(numero)
        print(f"{numero} ",end="", flush=True)
        sleep(0.2)
    print("Pronto.")


def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"Somando os valores pares de {lista}, temos {soma}")


numeros = list()
sorteia(numeros)
soma_par(numeros)