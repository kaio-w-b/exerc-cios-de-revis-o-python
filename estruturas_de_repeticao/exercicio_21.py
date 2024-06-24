"""
    Escreva um list comprehension que lista os números do conjunto dos numeros
    pares entre 0 e 100
"""

lista = [x * 2 for x in range(0,51)]

for x in lista:
    print(lista[x] * 1.5)
