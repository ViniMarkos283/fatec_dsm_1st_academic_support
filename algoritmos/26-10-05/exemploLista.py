# inicializa a lista chamada L, ela possuirá 5 strings dentro dela, sendo cada uma delas um nome qualquer
L = ["Rafael", "Juliana", "Henrique", "Camila", "Thiago"]
#      [0]        [1]          [2]        [3]        [4]

i = 0                           # inicializa o contador I com o valor inicial de zero

while i < 5:                    # enquanto I for menor que 5 (valor que não existe dentro da lista)...
    print(f'L[{i}] = {L[i]}')   # imprimimos a posição do item da lista junto ao valor guardado nessa posição
    i += 1                      # o contador I sobe 1 na contagem

print('Fim')                    # após o termino do loop, imprimimos o fim da operação