"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente
de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule
e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import datetime


dados = dict()

dados["Nome"] = str(input("Nome: "))
nasc = int(input("Ano de Nascimento: "))
dados["Idade"] = datetime.now().year - nasc
dados["ctps"] = int(input("Carteita de Trabalho (0 não tem): "))
if dados["ctps"] != 0:
    dados["Contratação"] = int(input("Ano de Contratação: "))
    dados["Salário"] = float(input("Salário: R$"))
    dados["Aposentadoria"] = dados["Idade"] + ((dados['Contratação'] + 35) - datetime.now().year)

for chave, valor in dados.items():
    print(" - {} tem o valor {}.".format(chave, valor))