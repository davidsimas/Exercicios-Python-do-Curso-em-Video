"""
Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
escolhido pelo computador. O programa deverá escrever na tela se o usuário
venceu ou perdeu.
"""
from random import randint
from time import sleep


computador = randint(0, 5)
print("-=-" * 20)
print("vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)
jogador = int(input("Em que número eu pensei? "))

print("Processando...")
sleep(2)

if jogador == computador:
    print("Parabéns! Voçê conseguiu me vencer!")
else:
    print("Ganhei! Eu pensei no número {} e não no {}!".format(computador, jogador))
