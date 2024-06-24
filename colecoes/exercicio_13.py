"""
    Imagine que você precise contar as ocorrências das letras C, G, A e T
    correspondentes ás bases nitrogenadas do DNA, em uma string. Crie um 
    programa com uma variável dna, contendo a sequência 'CGCGGACCTTTCCCAAA',
    que immprima na saída o número de ocorrências de cada letra
"""

dna = 'CGCGGACCTTTCCCAAA'

contagem_C = dna.count('C')
contagem_G = dna.count('G')
contagem_A = dna.count('A')
contagem_T = dna.count('T')


print(f'C: {contagem_C}')
print(f'G: {contagem_G}')
print(f'A: {contagem_A}')
print(f'T: {contagem_T}')