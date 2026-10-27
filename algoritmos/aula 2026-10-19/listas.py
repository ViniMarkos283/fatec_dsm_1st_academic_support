# criação de uma lista
L = []
L = list()

# acessar um item da lista
L[2]                                # indice da posição desejada

# atualizar  um item da lista
L[2] = 123

# buscar um item na lista
20 in L                             # verificase o item está em L
20 not in L                         # verifica se o item não está em L

# criação de lista com itens
L = [10, True, 3.14, "oi"]          # criando uma lista heterogenea (varios tipos de variaveis juntas)
L = list('abracadabra')             # criando uma lista diretamente na atribuição de conteudo da variavel

# adicionar um item na lista
L.append(20)                        # adiciona o 20 na ultima posição da lista, exemplo: a lista tem 3 valores, esse 20 virará o quarto valor
L.insert(0,30)                      # (posição, valor)

# remover um item da lista
L.remove(3.14)                      # remove pelo valor
del L[1]                            # remove pelo indice
