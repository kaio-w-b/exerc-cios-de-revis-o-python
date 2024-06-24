"""
    Altere o programa anterior, acrescente uma variavel chamada teste2, contendo
    os números inteiros de 6 a 10. Acrescente a essa lista à primeira, 
    estendento-a, e em seguida, imprima a nova lista gerada
"""

teste = [1,2,3,4,5]
teste2 =[6,7,8,9,10]

print(f'O segundo  elemento da lista eh: {teste[1]}')

print(f'A lista com todos os elementos eh: {teste}')

teste.extend(teste2)

print(f'A nova lista agora eh: {teste}')