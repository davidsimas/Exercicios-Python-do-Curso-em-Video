"""
Escreva um programa em Python que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
"""


num = int(input("Digite um número inteiro: "))

print("""Escolha uma das bases para conversão
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal
""")
opcao = int(input("Sua opção: "))

if opcao == 1:
    print("{} convertido para Binário é igual a {}".format(num, bin(num)[2:]))
elif opcao == 2:
    print("{} convertido para Octal é igual a {}".format(num, oct(num)[2:]))
elif opcao == 3:
    print("{} convertido para Binário é igual a {}".format(num, hex (num)[2:]))
else:
    print("opção inválida, tente novamente.")

