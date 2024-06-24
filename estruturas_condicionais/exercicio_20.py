"""
    Escreva um programa que ista os números entre 5000 e 10000 que são divisíveis
    simultaneamente, por 3 e 7.
"""
lista =[]
for x in range(5000,10001):
    if(x % 3 == 0) and (x % 7 == 0):

        lista.append(x)
        
print(f'A lista de valores divisiveis por 3 e por 7 simultaneamente são: \
{lista}')

     