"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados
de cada pessoa em um dicionário e todos os dicionários em uma lista. No final,
mostre: 

A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""


galera = list()
pessoa = dict()
soma = 0
media = 0

while True:
    pessoa.clear()
    pessoa["Nome"] = str(input("Nome: "))
    while True:
        pessoa["Sexo"] = str(input("Sexo: [M/F] ")).strip().upper()[0]
        if pessoa["Sexo"] in "MF":
            break
        print("Erro. Por favor, digite apenas M ou F.")
    pessoa["Idade"] = int(input("Idade: "))
    soma += pessoa["Idade"]
    galera.append(pessoa.copy())

    while True:
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if resp in "SN":
            break
        print("Erro. Responda apenas S ou N.")
    if resp == "N":
        break

print("-=" * 30)
print("A) Ao todo temos {} pessoas cadastradas.".format(len(galera)))

media = soma / len(galera)
print("B) A média de idade é de {:5.2f} anos.".format(media))
print("C) As mulheres cadastradas foram ", end="")
for pessoa in galera:
    if pessoa["Sexo"] in "Ff":
        print("{} ".format(pessoa["Nome"]), end="")
print()

print("D) Lista das pessoas que estão acima de média: ", end="")
for pessoa in galera:
    if pessoa["Idade"] >= media:
        print("    ")
        for chave, valor in pessoa.items():
            print("{} = {}; ".format(chave, valor), end="")
        print()
print("<< Encerrado >>")