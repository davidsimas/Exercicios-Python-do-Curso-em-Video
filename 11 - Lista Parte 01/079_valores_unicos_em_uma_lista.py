"""
Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.
"""


numeros = list()

while True:
    num = int(input("Digite um valor: "))
    
    if num not in numeros:
        # Adiciona valor a lista.
        numeros.append(num)
        print("Valor adicionado com sucesso.")
    else:
        print("Valor duplicado.")
    
    resp = str(input("Quer continuar? [S/N]"))
    if resp in "Nn":
        break

print("-=" * 30)
# Ordena a lista em ordem crescente.
numeros.sort()
print("Você digitou os valores {}".format(numeros))