"""
    Converta o codigo da questão anterior em uma função de nome delta(), sem pârametros.
    como fazer para passar os valores de a, b e c para delta()?
    
"""
a = 4.5
b = 10
c = 3

def delta():
    return(b**2 - 4*a*c)

print(f'O resultado da funcao delta eh: {delta()}')

#podemos fazer a função delta() funcionar utilizando a, b e c como variaveis globais