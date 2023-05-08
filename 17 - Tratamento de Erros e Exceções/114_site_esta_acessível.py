"""
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""
import urllib
import urllib.request


try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.URLError:
    print("O site Pudim não está acessível no momenro.")
else:
    print("Consegui acessar o site Pudim com sucesso.")
    # Ler o conteúdo do site em HTML.
    print(site.read())