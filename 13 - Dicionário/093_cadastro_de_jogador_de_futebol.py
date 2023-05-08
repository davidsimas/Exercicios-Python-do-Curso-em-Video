"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai
ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""


jogador = dict()
partidas = list()

jogador["Nome"] = str(input("Nome do Jogador: "))
total = int(input("Quantas partidas {} jogou? ".format(jogador["Nome"])))

for cont in range(0, total):
    partidas.append(int(input(" - Quantos gols na partida {}? ".format(cont + 1))))

jogador["Gols"] = partidas[:]
jogador["Total"] = sum(partidas)

print("-=" * 30)
print(jogador)

print("-=" * 30)
for chave, valor in jogador.items():
    print("O campo {} tem o valor {}".format(chave, valor))

print("-=" * 30)
print("O jogador {} jogou {} partidas.".format(jogador["Nome"], len(jogador["Gols"])))
for indice, valor in enumerate(jogador["Gols"]):
    print("   => Na partida {}, fez {} gols.".format(indice + 1, valor))
print("Foi um total de {} gols.".format(jogador["Total"]))