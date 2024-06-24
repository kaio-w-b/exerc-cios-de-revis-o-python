"""
    crie uma variável denominada eh_impar e inicialize-a com o resultado de
    (57%2==0). Imprima seu conteudo na tela. Por que o resultado foi um booleano,
    e não um valor numérico?
"""

eh_impar = (57%2==0)
print(f'eh_impar = {eh_impar}!')

# O resultado é um booleano pois, por conta da igualdade "==" é feita uma comparação
# sendo ela: "o resto da divsão de 57 por 2 é 0" o que retorna False