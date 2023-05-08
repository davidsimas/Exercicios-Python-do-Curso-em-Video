"""
Escreva um programa que leia um valor em metros e o exiba convertido em 
centímetros e milímetros.
"""


medida = float(input("Digite uma distância em metros: "))
cm = medida * 100
mm = medida * 1000

print("A média de {}M corresponde a {:.0f}cm e {:.0f}mm.".format(medida, cm, mm))

"""
dm(Decímetro) é igual a:  valor * 10
cm(Centrímetro) é igual a:  valor * 100
mm(Milímetro) é igual a:  valor * 1000
dam(Decâmetro) é igual a:  valor / 10
hm(Hectômetro) é igual a: valor / 100
km(Quilômetro) é igual a: valor / 1000
"""