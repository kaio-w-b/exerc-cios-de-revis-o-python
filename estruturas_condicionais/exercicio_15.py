"""
    Crie um programa com três variáveis, lado1, lado2 e lado3, e inici-as com
    quaisquer valor númericos. Imprima na saída se esses tamanhos de lados 
    formam ou não um triangulo
"""

lado1 = 3
lado2 = 8
lado3 = 10

if(lado2 + lado3 > lado1) and(lado2 + lado3 > lado2) and \
    (lado1 + lado2 > lado3):
        print('Os valores fornecidos formam um triangulo')
        
else:
    print('Os valores fornecidos nao formam um triangulo')
    