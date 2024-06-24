"""
    Crie uma função que recebe a altura, a largura e o comprimento em metros
    de um tanque cúbico e retorna a capacidade em litros do tanque.
"""

def volume_em_litros(altura,largura,comprimento):
    resultado_em_m3 = altura* largura * comprimento
    resultado_em_litros= resultado_em_m3 * 1000
    return resultado_em_litros
