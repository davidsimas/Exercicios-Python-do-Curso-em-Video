"""
Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo
que cada litro de tinta pinta uma área de 2 metros quadrados.
"""


largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))

area = largura * altura
tinta = area / 2

print("Sua parede tem a dimensão de {} x {} e sua área é de {}M²".format(largura, altura, area))
print("Para pintar essa parede, voçê precisará de {}L de tinta". format(tinta))