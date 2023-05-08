"""
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um
sistema de visualização de detalhes do aproveitamento de cada jogador.
"""


time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador["Nome"] = str(input("Nome do Jogador: "))
    total = int(input("Quantas partidas {} jogou? ".format(jogador["Nome"])))
    partidas.clear()

    for cont in range(0, total):
        partidas.append(int(input(" - Quantos gols na partida {}? ".format(cont + 1))))

    jogador["Gols"] = partidas[:]
    jogador["Total"] = sum(partidas)

    time.append(jogador.copy())

    while True:
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()
        if resp in "SN":
            break
        print("Erro, responda apenas S ou N.")
    if resp == "N":
        break

# Imprime um cabeçalho.
print("-=" * 30)
print("Cod ", end="")
for i in jogador.keys():
    print("{:<15}".format(i), end="")
print()
print("-" * 40)
for chave, valor in enumerate(time):
    print("{:>3} ".format(chave), end="")
    for dados in valor.values():
        print("{:<15}".format(str(dados)), end="")
    print()
print("-" * 40)

while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar.) "))
    if busca == 999:
        break
    if busca >= len(time):
        print("Erro. Não existe jogador com o código {}".format(busca))
    else:
        print(" == Levantamento do Jogador {}:".format(time[busca]["Nome"]))
        for indice, gol in enumerate(time[busca]["Gols"]):
            print("     No jogo {} fez {} gols.".format(indice + 1, gol))
    print("-" * 40)
print(" << volte Sempre >>")