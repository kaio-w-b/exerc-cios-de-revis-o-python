"""
    Altere o programa anterior, acrescentando uma variável chamada numeros_extenso,
    contendo os números da questão anterior escritos por extenso, e uma lista
    composta, contendo as duas listas anteriores. Imprima seus conteúdos na 
    saída padrão. Imprima o valor numérico e por extenso do primeiro e do ultimo
    elemento da lista.
"""

valores = [1,2,3,4,5,6,7,8,9,10]
numeros_extenso = ['um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
                  'oito', 'nove', 'dez']
lista_composta =[valores,numeros_extenso]

print(f'Conteudo da lista: {lista_composta}')
print(f'primeiro elemento da lista: {lista_composta[0][0]} - {lista_composta[1][0]}')

print(f'ultimo elemento da lista: {lista_composta[0][9]} - {lista_composta[1][9]}')
