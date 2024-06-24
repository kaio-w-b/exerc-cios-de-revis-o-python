"""
    Altere a questão 26 do exercícios para receber, também, o preço de um litro de 
    água e calcular qual o custo para encher o mesmo tanque.
"""

def volume_em_litros(altura,largura,comprimento,preco_litro):
    resultado_em_m3 = altura* largura * comprimento
    resultado_em_litros= resultado_em_m3 * 1000
    preco_total = preco_litro * resultado_em_litros
    return preco_total
