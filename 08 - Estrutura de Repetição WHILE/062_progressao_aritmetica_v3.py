"""
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais
alguns termos. O programa encerrará quando ele disser que quer mostrar 0
termos.
"""


print("Gerador de PA")
print("-=" * 10)

termo = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))

cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print("{} → ".format(termo), end = "")
        termo += razao
        cont += 1
    print("Pausa")
    mais = int(input("Qunatos termo você quer mostrar a mais? "))
print("Progressão finalizada com {} termos mostrados.".format(total))