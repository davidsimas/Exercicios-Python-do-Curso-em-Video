"""
Faça um programa que tenha uma função notas() que pode receber várias notas de
alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
"""


def notas(*notas, sit=False):
    """
    -> Funções para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :retun: dicionário com várias informações sobre a situacão de turma.
    """
    r = dict()
    r["Total"] = len(notas)
    r["Maior"] = max(notas)
    r["Menor"] = min(notas)
    r["Média"] = sum(notas) / len(notas)

    if sit:
        if r["Média"] >= 7:
            r["Situação"] = "Boa"
        elif r["Média"] >= 5:
            r["Situação"] = "Razoável"
        else:
            r["Situação"] = "Ruim"

    return r


# Programa principal
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)