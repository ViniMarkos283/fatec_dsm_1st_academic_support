'''
    crie um programa que solicite diversas
    idades e exiba a da pessoa mais jovem.
    ao final, tambem exiba a média das idades
    e exiba todas as idades abaixo da média
    OBS: considere 'diversas' como todas as
    idades antes da primeira negativa
'''

def coleta_idades() -> list:                                # função para coleta de idades, deverá devolver uma lista no final
    idades = []                                                 # inicia uma lista vazia chamada idades
    i = 1                                                       # inicia um contador direto no 1
    idade = int(input(f'{i} idade: '))                          # pede que o usuario informe uma idade
    while idade >= 0:                                           # enquanto a idade não for um valor negativo...
        idades.append(idade)                                    # a lista idades recebe a idade informada pelo usuario
        i +=1                                                   # o contador acrescenta 1
        idade = int(input(f'{i} idade: '))                      # ele volta a perguntar novamente a idade ao usuario
    return idades                                               # ao fim do loop, devolvemos a lista idades preenchida

def menor_idade(idades:list) -> int:                        # função que recebe uma lista de idades e devolve o valor da menor idade da lista
    m = idades[0]                                               # a menor idade será sempre a primeira da lista, após a conferencia das demais, esse valor pode mudar
    i = 1                                                       # inicia-se o contador no valor 1 (a zero é a idade que colocamos como menor, então ignoramos ela)
    while i < len(idades):                                      # enquanto o contador for menor q o tamanho maximo da lista de idades...
        if idades[i] < m:                                       # conferimos se a idade é menor q a primeira da lista, se ela for...
            m = idades[i]                                       # o valor atual passa a ser a menor idade
        i += 1                                                  # o contador sobe 1
    return m                                                    # após conferir todas, devolvemos a menor idade obtida

def media_idades(idades:list) -> float:                     # função que pega a lista de idades e devolve a média entre elas
    soma = 0                                                    # variavel q vai receber a soma de todas as idades
    qtd = 0                                                     # variavel q vai contar quantas idades tem, e dps usaremos ela pra dividir a soma
    while qtd < len(idades):                                    # enquanto o contador de idades for menor q o tamanho maximo da lista...
        soma += idades[qtd]                                     # somamos a idade ao somador
        qtd += 1                                                # contamos 1 pra cada idade somada
    return soma / qtd                                           # devolvemos a divisão da soma com a quantidade de idades 

def abaixo_media(idades:list(int), media:float) -> None:    # função que devolve uma lista das idades que forem menores q a média entre elas
    i = 0                                                       # contador iniciado em zero
    while i < len(idades):                                      # enquanto o contador for menor q o tamanho maximo da lista...
        if idades[i] < media:                                   # conferimos se a idade é menor q a média, se for...
            print(idades[i])                                    # imprimimos ela
        i += 1                                                  # o contador ganha 1

def main():                                                 # função main, onde o script começa a rodar
    idades = coleta_idades()                                    # obtemos a lista de idades com a função que as coleta
    jovem = menor_idade(idades)                                 # obtemos o menor valor entre elas com uma função que as compara
    print(f'Mais jovem: {jovem} anos')                          # dizemos ao usuario qual idade é a menor
    media = media_idades(idades)                                # obtemos a média com uma função que a calcula
    print(f'Média: {media:.1f} anos')                           # dizemos ao usuario a média devolvida pela função
    print(f'idades abaixo da média: ')                          # dizemos q abaixo mostraremos todas as idades abaixo da média
    abaixo_media(idades, media)                                 # imprimimos pela função todas as idades menores que a média

'''
    Explicação do if abaixo:
    se estiver rodando varios arquivos python juntos, ele confere o nome do arquivo atual
    e se o mesmo se chamar main, ele inicia o script aqui, senão ele ignora.
    È util pra evitar varios arquivos distintos de rodarem sem q sejam chamados.
    Se esse script rodar sozinho, sem importações, o  name dele sempre será main, msm q o nome do 
    arquivo seja diferente.
'''
if __name__ == '__main__': 
    main()
