"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""


times = ("Corinthians", "Palmeiras", "Santos", "Grêmio",
         "Cruzeiro", "Flamengo", "Vasco", "Chapecoense",
         "Atlético", "Botafogo", "Atlético-PR", "Bahia",
         "São Paulo", "Fluminense", "Sport Recife",
         "EC Vitória", "Coritiba", "Avaí", "ponte Preta",
         "Atlético_GO")

print("-=" * 15)
#print("Lista de times: {}".format(times))
for time in times:
    print(time)

print("-=" * 15)

# Os 5 primeiros times
print("Os 5 primeiros são {}".format(times[0:5]))

# Os últimos 4 colocados.
print("-=" * 15)
print("Os últimos 4 colocados são {}".format(times[-4:]))

# Times em ordem alfabética.
print("-=" * 15)
print("Times em ordem alfabética: {}".format(sorted(times)))

# Em que posição está o time da Chapecoense.
print("-=" * 15)
print("O chapecoense está na {}ª posição".format(times.index("Chapecoense") + 1))