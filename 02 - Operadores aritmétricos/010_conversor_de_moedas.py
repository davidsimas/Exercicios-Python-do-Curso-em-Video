"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
"""


real = float(input("Quanto dinheiro voçê tem? R$"))

dolar = 3.27

print("Com R${:.2f} voçê pode comprar US${:.2f}".format(real, (real / dolar)))