"""
Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep


num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))

opcao = 0
while opcao != 5:
    print("""
    [ 1 ] somas
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do proggrama
    """)
    opcao = int(input("Qual é a sua opção? "))

    if opcao == 1:
        soma = num1 + num2
        print("A soma entre {} e {} é {}".format(num1, num2, soma))
    elif opcao == 2:
        produto = num1 * num2
        print("O resultado de {} x {} é {}".format(num1, num2, produto))    
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print("Entre {} e {} o maior valor é {}".format(num1, num2, maior))
    elif opcao == 4:
        print("Informe os números novamentes:")
        num1 = int(input("Primeiro valor: "))
        num2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Finalizando")
    else:
        print("Opção inválida, Tente novamente.")
    print("=-=" * 10)
    sleep(1)

print("Fim do programa, Volte sempre.")