"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto
qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

Ex: 
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~~~~
"""


def escreva(msg):
    tamanho = len(msg) + 4
    print("~" * tamanho)
    print("  {}".format(msg))
    print("~" * tamanho)


# Programa principal
escreva("David Simas")
escreva("Olá, Mundo")
escreva("Curso de Python do Curso em Video")