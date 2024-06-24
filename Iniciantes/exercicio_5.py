"""
    Declare três variáveis denominadas palavra, numero e booleano e atribua-lhes
    os valores iniciais "Teste", 15 e True. Em seguida, imprima duas linhas que
    mostram seus conteúdos, interpolados com textos. Para a primeira linha, use
    o operador %, e, para a segunda, utilize uma f-string. Seu resultado deve
    ser semelhante a:
        Usando %: palavra='teste',numero=15 e booleano = True.
        usando f-string:palavra= 'teste',numero =15 e booleano = True.
"""

palavra = '\'teste\''
numero = 15
booleano = True

print('Usando %%: palavra = %s, numero = %d e booleano = %s' %(palavra,numero,booleano))

print(f'usando f-string: palavra ={palavra}, numero ={numero} e booleano ={booleano}')