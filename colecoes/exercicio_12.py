"""
    crie um conjunto com o nome primos, contendo os números primos menores que
    20, um conjunto chamado pares com os numeros pares de 0 a 10, e outro,
    chamado umoares, contendo os numeros ímpares entre 10 e 20. Imprima o
    resultado de: Pares[uniao](primos[intersecão]impares)
    
"""
primos = {2,3,5,7,11,13,17}

pares = {2,4,6,8,10}

impares = {11,13,15,17,19}

resultado = pares|(primos & impares)

print(f'O resultado da oprecao eh: {resultado}')