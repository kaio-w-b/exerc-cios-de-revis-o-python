"""
    Crie um programa com três variáveis lado1, lado2 e lado3, e inicie-as com
    quaisquer valores numéricos. Imprima na saída se esses tamanhos de lados 
    formam ou não um triangulo retângulo.
"""

lado1 = 3
lado2 = 4
lado3 = 5

if(lado3**2 == lado1 **2 + lado2 **2) or (lado2 **2 == lado1 **2 + lado3 **2) \
    or (lado1 **2 == lado2 **2 + lado3 **2):
        print('O triangulo formado eh quadrado')
        
else:
    print('O triangulo formado nao eh quadrado')
