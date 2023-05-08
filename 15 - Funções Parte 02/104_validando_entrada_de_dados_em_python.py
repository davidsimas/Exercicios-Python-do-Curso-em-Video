"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
semelhante 'a função input() do Python, só que fazendo a validação para aceitar
apenas um valor numérico.

Ex: n = leiaInt('Digite um n: ')
"""


def leia_int(msg):
    ok = False
    valor = 0
    while True:
        numero = str(input(msg))
        if numero.isnumeric():
            valor = int(numero)
            ok = True
        else:
            print("Erro, digite um número inteiro válido.")
        if ok:
            break
    return valor


# Programa principal
num = leia_int("Digite um número: ")
print(f"Você acabou de digitar o número {num}")