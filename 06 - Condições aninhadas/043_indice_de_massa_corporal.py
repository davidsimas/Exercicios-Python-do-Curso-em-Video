"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela
abaixo:

- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""


peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é a sua altura? (M) "))

imc = peso / (altura ** 2)

print("O IMC dessas pessoa é de {:.2f}".format(imc))

if imc < 18.5:
    print("Você está Abaixo do peso normal.")
elif imc >= 18.5 and imc < 25:
    print("Parabéns, você está na faixa de peso normal.")
elif imc >= 25 and imc < 30:
    print("Você está em Sobrepeso.")
elif imc >= 30 and imc < 40:
    print("Você está em Obesidade.")
else:
    print("Você está em Obesidade Mórbida, cuidado.")