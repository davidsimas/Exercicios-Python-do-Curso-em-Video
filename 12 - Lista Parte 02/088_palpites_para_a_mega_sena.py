"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6
números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
composta.
"""
from random import randint
from time import sleep


lista = list()
jogos = list()

print("-" * 30)
print("      JOGA NA MEGA SENA      ")
print("-" * 30)

quant = int(input("Quantos jogos você quer que eu sorteie? "))
total = 1

while total <= quant:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print("-=" * 3, " SORTEANDO 6 JOGOS ", "-=" * 3)
for indice, lista in enumerate(jogos):
    print("Jogo {}: {}".format(indice + 1, lista))
    sleep(1)
print("-=" * 5, "< BOA SORTE. >", "-=" *5)