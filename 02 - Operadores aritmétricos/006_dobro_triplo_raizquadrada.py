"""
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""


num = int(input("Digite um número: "))

doblo = num * 2
triplo = num * 3
raiz = num ** (1 / 2)

print("O bodro de {} vale {}.".format(num, doblo))
print("O triplo de {} vale {}.".format(num, triplo))
# Duas casas decimais flutuantes.
print("A raiz quadrada de {} vale {:.2f}.".format(num, raiz))

# Ou de forma direta, \n para quebra de linha.
print("\nDe forma direta\n")

print("O bodro de {} vale {}.".format(num, (num * 2)))
print("O triplo de {} vale {}.".format(num, (num * 3)))
# Duas casas decimais flutuantes.
print("A raiz quadrada de {} vale {:.2f}.".format(num, (pow(num, (1 / 2)))))