'''
    crie um programa que solicite diversas
    idades e exiba a da pessoa mais jovem.
    ao final, tambem exiba a média das idades
    e exiba todas as idades abaixo da média
    OBS: considere 'diversas' como todas as
    idades antes da primeira negativa
'''

def coleta_idades() -> list:
    idades = []
    i = 1
    idade = int(input(f'{i} idade: '))
    while idade >= 0:
        idades.append(idade)
        i +=1
        idade = int(input(f'{i} idade: '))
    return idades

def menor_idade(idades:list) -> int:
    m = idades[0]
    i = 1
    while i < len(idades):
        if idades[i] < m:
            m = idades[i]
        i += 1
    return m

def media_idades(idades:list) -> float:
    soma = 0
    qtd = 0
    while qtd < len(idades):
        soma += idades[qtd]
        qtd += 1
    return soma / qtd

def abaixo_media(idades:list(int), media:float) -> None:
    i = 0
    while i < len(idades):
        if idades[i] < media:
            print(idades[i])
        i += 1

def main():
    idades = coleta_idades()
    jovem = menor_idade(idades)
    print(f'Mais jovem: {jovem} anos')
    media = media_idades(idades)
    print(f'Média: {media:.1f} anos')
    print(f'idades abaixo da média: ')
    abaixo_media(idades, media)

if __name__ == '__main__':
    main()
