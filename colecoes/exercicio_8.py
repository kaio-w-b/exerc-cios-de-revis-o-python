"""
    a) Crie uma lista vazia, denominada itens, e acrescente a ela três strings:
    "livro","caderno" e "borracha"
    
    b) Altere o item de ìndice 1 para "régua".
    
    c) Verifique se o item "caderno" ainda esta na lista.
    
    d) Imprima a quantidade de elementos da lista, remova o último elemento da
    lista e imprima-o; em seguida, imprima o novo tamanho da lista
    
    e) Crie uma variável chamada fatia, que contenha os dois ultimos elementos 
    da lista e imprima-a na saída padrão.
"""

itens = []
itens.append("livro")
itens.append("caderno")
itens.append("borracha")

itens[1] = "regua"

if('caderno' in itens):
    print('O caderno esta na lista')
    
print(f'O tamanho da lista de itens eh de {len(itens)}')

ultimo_elemento = itens.pop()

print(f'O ultimo elemento da lista antes de ser removido era: {ultimo_elemento}')

print(f'O novo tamanho da lista agora eh: {len(itens)}')

fatia = itens[-2:]

print(f'Os dois ultimos elementos da lista sao: {fatia}')