from lib.interface import *
from lib.arquivo import *


arq = "cursoemvideo.txt"

if arquivo_existe(arq):
    print("Arquivo encontrado cpm sucesso.")
else:
    print("Arquivo não encontrado.")
    criar_arquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas",
                     "Cadastrar nova Pessoas",
                     "Sair do Sistema"])

    match resposta:
        case 1:
            # Opção de listar o conteúdo de um arquivo.
            ler_arquivo(arq)
        case 2:
            # Opção de cadastrar uma nova pessoa.
            cabecalho("Novo Cadastro")
            nome = str(input("Nome: "))
            idade = int(input("Idade: "))
            cadastrar(arq, nome, idade)
        case 3:
            # Opção de sair do sistema.
            cabecalho("Saindo do sistema... Até logo.")
            break
        case _:
            # Digitou uma opção errada no menu.
            print("\033[31mERROR. Digite uma opção válida.\033[m")