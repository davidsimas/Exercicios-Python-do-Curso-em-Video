"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
"""


total18 = 0
total_homens = 0
total_mulher20 = 0

while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).upper().strip()[0]
    
    if idade >= 18:
        total18 += 1
    if sexo == "M":
        total_homens += 1
    elif sexo == "F" and idade < 20:
        total_mulher20 += 1

    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resp == "N":
        break

print("Total de pessoas com mais de 18 anos: {}".format(total18))
print("Ao todo temos {} homens cadastrados.".format(total_homens))
print("E temos {} mulheres com menos de 20 anos.".format(total_mulher20))