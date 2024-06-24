"""
    Faça um programa que crie três variáveis, var1, var2 e var3. Atribua qualquer
    valor numérico às variáveis e imprima qual é a mediana delas e seu valor.
"""

var1 = 1 
var2 = 2 
var3 = 3 

if((var1 > var2) and (var1 < var3)) or ((var1 < var2) and (var1 > var3)):
    print(f'A mediana dos valores eh = {var1}')

elif((var2 > var1) and (var2 < var3)) or ((var2 < var1) and (var2 > var3)):
    print(f'A mediana dos valores eh = {var2}')

else:
    print(f'A mediana dos valores eh = {var3}')