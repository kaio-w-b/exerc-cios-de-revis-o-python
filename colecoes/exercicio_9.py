"""
    Altere a questâo anterior para, após as operações da questão, inserir
    string "livro" na posição 0 da lista itens e, em seguida, imprimir o novo
    conteudo da mesma.
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

itens.insert(0, "livro")

print(f'Após a inserção do novo elemento {itens}')