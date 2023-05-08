"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de
um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""


def area(largura, comprimento):
    area = largura * comprimento
    print("A área de um terreno {} x {} é de {}m².".format(largura, comprimento, area))



# Programa principal.
print(" Controle de Terrenos")
print("-" * 20)
lar = float(input("Largura (M): "))
comp = float(input("Comprimento (M): "))

# Chamando a função.
area(lar, comp)