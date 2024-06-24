"""
    Crie uma função que recebe as coordenadas (x,y) de dois pontos no plano
    cartesiano e imprime e retorna o coeficiente angular da reta formada por
    eles.
"""

def coeficiente_angular(x1,y1,x2,y2):
    resultado = 0
    delta_y = y2 - y1
    delta_x = x2 - x1
    
    if(delta_x == 0):
        print('Reta vertical - coeficiente angular -> infinito')
    else:
        resultado = delta_y / delta_x
        print(f'O coeficiente angular da reta formada por({x1},{y1}) é \
({x2},{y2}) é: {resultado}')
    
    return resultado
