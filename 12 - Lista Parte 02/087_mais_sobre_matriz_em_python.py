"""
Aprimore o desafio anterior, mostrando no final: 

A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = 0
maior = 0
soma_coluna = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input("Digite um valor para [{}, {}]: ".format(linha, coluna)))

print("-=" * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")
        # A soma de todos os valores pares digitados.
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
    print()
print("-=" * 30)
print("A soma dos valores pares é {}".format(soma_par))
# A soma dos valores da terceira coluna.
for linha in range(0, 3):
    soma_coluna += matriz[linha][2]
print("A soma dos valores da terceira coluna é {}".format(soma_coluna))
# O maior valor da segunda linha.
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print("O maior valor da segunda linha é {}".format(maior))