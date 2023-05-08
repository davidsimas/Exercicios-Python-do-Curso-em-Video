"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse
dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from operator import itemgetter


jogo = {"Jogador1": randint(1, 6),
        "Jogador2": randint(1, 6),
        "Jogador3": randint(1, 6),
        "Jogador4": randint(1, 6),}

ranking = list()

print("Valores sorteados:")
for chave, valor in jogo.items():
    print("{} tirou {} no dado.".format(chave, valor))

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print("-=" * 20)
print("  == Ranking dos Jogadores ==")
for indice, valor in enumerate(ranking):
    print("   - {}º lugar: {} com {}.".format(indice + 1, valor[0], valor[1]))