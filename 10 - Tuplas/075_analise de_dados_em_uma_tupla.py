"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""


num = (int(input("Digite um número: ")),
       int(input("Digite um número: ")),
       int(input("Digite um número: ")),
       int(input("Digite um número: ")))

print("Você digitou os valores {}".format(num))

# Quantas vezes apareceu o valor 9.
print("O valor 9 apareceu {} vezes.".format(num.count(9)))

# Em que posição foi digitado o primeiro valor 3.
if 3 in num:
    print("O valor 3 apareceu na {}ª posição.".format(num.index(3) + 1))
else:
    print("O valor 3 não foi digitado em nenhuma posição.")

# Quais foram os números pares.
print("Os valores pares digitados foram: ", end = "")
for n in num:
    if n % 2 == 0:
        print(n, end = " ")