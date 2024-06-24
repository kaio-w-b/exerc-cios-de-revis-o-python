"""
    O trecho de programa a seguir inicializa a variável numero_aleatorio com um
    valor randômico inteiro. Pede-se: altere o programa para que ele imprima na 
    tela o valor que foi usado na execução atual, e se esse valor é positivo,
    negativo ou neutro
    
    trecho fornecido:
        import random
        numero_aleatorio = random.randint(-100,101)
"""

import random
numero_aleatorio = random.randint(-100, 101)

if (numero_aleatorio > 0):
    print(f'O numero {numero_aleatorio} eh positivo.')
    
elif(numero_aleatorio < 0):
    print(f'O numero {numero_aleatorio} eh negativo.')
    
else:
    print(f'O numero {numero_aleatorio} eh neutro.')
    