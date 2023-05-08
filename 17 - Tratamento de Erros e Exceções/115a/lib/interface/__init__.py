def leia_int(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return numero


def linha(tam=42):
    return "-" * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho("Menu Principal")
    cont = 1
    for item in lista:
        print(f"\033[33m{cont}\033[m - \033[34m{item}\033[m")
        cont += 1
    print(linha())
    opcao = leia_int("\033[32mSua Opção: \033[m")
    return opcao