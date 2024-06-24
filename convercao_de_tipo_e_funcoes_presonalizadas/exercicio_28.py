"""
    Crie uma função que recebe as coordenadas (x,y) de dois pontos no plano 
    cartesiano e imprime a distância entre eles.
"""
from math import sqrt

def distancia(x1,y1,x2,y2):
    resultado = sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    print(f'A distancia dos pontos ({x1},{y1}) e ({x2},{y2}) é: {resultado}')
    return resultado
    