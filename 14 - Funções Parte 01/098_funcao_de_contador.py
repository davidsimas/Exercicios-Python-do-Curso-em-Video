"""
Faça um programa que tenha uma função chamada contador(), que receba três
parâmetros: início, fim e passo. Seu programa tem que realizar três contagens
através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
from time import sleep


def contador(inicio, fim, passo):

    # Se o passo estiver com valor negativo, multiplica por -1 para inverter.
    if passo < 0:
        passo *= -1
    # Se o passo estiver com valor 0, passo assume valor 1.
    if passo == 0:
        passo = 1

    print("Contagem de {} até {} de {} em {}.".format(inicio, fim, passo, passo))


    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print("{} ".format(cont), end="", flush=True)
            sleep(0.2)
            cont += passo
        print("Fim")
    else:
        cont = inicio
        while cont >= fim:
            print("{} ".format(cont), end="", flush=True)
            sleep(0.2)
            cont -= passo
        print("Fim")     

# Programa principal.
contador(1, 10, 1)
contador(10, 0, 2)

print("Agora é sua vez de personalizar a contagem.")

ini = int(input("Início: "))
fim = int(input("Fim: "))
pas = int(input("Passo: "))

contador(ini, fim, pas)