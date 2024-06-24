"""
    Crie uma função que recebe como parâmetro a distância de um trajeto em km,
    o consumo em km\l de um meio de transportee= e informa quantos litros de
    combustível serâo nescessários para a viagem.
"""

def consumo(distancia_km,consumo_km_l):
    resultado = distancia_km/consumo_km_l
    print(f'Para essa viagem serao nescessarios {resultado} litros de combustivel')
    return resultado
