"""
    Escreva um programa que conta os números pares e divisíveis por 4 e 3 entre
    2000 e 5000
"""

lista = []

# como será verificado se o numero é divisível por 4 ele também será divisível
# por 2 assim sendo par
for x in range(2000,5001):
    if(x % 4 == 0) and (x % 3 == 0):
        lista.append(x)
        
print(f'Os numeros divisíveis por 3 e 4 simultaneamente são: {lista}')
    