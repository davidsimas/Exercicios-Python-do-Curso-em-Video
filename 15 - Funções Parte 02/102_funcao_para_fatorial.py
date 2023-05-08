"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado ou não na tela
o processo de cálculo do fatorial.
"""


# Função com Doc String
def fatorial(numero, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param numero: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número.
    """
    fat = 1
    for cont in range(numero, 0, -1):
        if show:
            print(cont, end="")
            if cont > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        fat *= cont
    return fat


# Programa principal
print(fatorial(5, show=True))
help(fatorial)