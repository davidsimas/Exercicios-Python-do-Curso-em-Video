"""
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que 
tipo de triângulo será formado:

- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
"""


print("-=" * 20)
print("Analisador de Triângulos")
print("-=" * 20)

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar um Triângulo.")
    if r1 == r2 == r3:
        print("Equilátero.")
    if r1 != r2 != r3 != r1:
        print("Escaleno.")
    else:
        print("Isósceles.")
    
else:
    print("Os segmentos acima não podem formar um Triângulo.")