"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o
sort()). No final, mostre a lista ordenada na tela.
"""


lista = []

for cont in range(0, 5):
    num = int(input("Digite um valor: "))

    if cont == 0 or num > lista[-1]:
        # Insere elemento na lista.
        lista.append(num)
        print("Adicionado ao final da lista.")
    else:
        posicao = 0
        while posicao < len(lista):
            if num <= lista[posicao]:
                # Insere elemento numa posição especifica.
                lista.insert(posicao, num)
                print("Adicionado na posição {}".format(posicao))
                break
            posicao += 1

print("-=" * 30)
print("Os valores digitados em ordem foram {}".format(lista))