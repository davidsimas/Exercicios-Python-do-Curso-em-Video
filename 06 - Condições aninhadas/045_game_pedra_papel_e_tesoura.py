"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""
from random import randint
from time import sleep


itens = ("Pedra", "Papel", "Tesuora")
computador = randint(0, 2)

print("""Suas opçôes:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
""")
jogador = int(input("Qual é a sua jogada? "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)

print("-=" * 10)
print("O computador jogou {}".format(itens[computador]))
print("O jogador jogou {}".format(itens[jogador]))
print("-=" * 10)

if computador == 0:
    if jogador == 0:
        print("Empate.")
    elif jogador == 1:
        print("Jogador Vence.")
    elif jogador == 2:
        print("Computador Vence.")
    else:
        print("Jogada inválida.")
elif computador == 1:
    if jogador == 0:
        print("Computador Vence.")
    elif jogador == 1:
        print("Empate.")
    elif jogador == 2:
        print("Jogador Vence.")
    else:
        print("Jogada inválida.")
elif computador == 2:
    if jogador == 0:
        print("Jogador Vence.")
    elif jogador == 1:
        print("Computador Vence.")
    elif jogador == 2:
        print("Empate.")
    else:
        print("Jogada inválida.")