"""
    Pesquise o algorítmo do "Crivo de Eratóstenes" -- um dos primeiros metodos
    para encontrar números primos, concebido séculos antes da invenção do 
    computador. Implemente um programa que imprima os números primos entre 0 e 100
"""

primos =[]

for x in range(2,101):
    eh_primo = True
    for y in primos:
        if(x % y == 0):
            eh_primo = False
            break
    if eh_primo:
        primos.append(x)
        
print(f'Os numeros primos estre 0 e 100 sao: {primos}')
        