'''
    Crie um programa que solicite ao usuario uma quantidade
    positiva de numeros e, em seguida, os n numeros.
    O programa deverá, ao final, exibir duas listas, uma
    com os primos digitados e a outra com os não primos.
'''

def eh_primo(x:int) -> bool:                                # define uma função que recebe um inteiro e retorna True ou False
    qtd_divisores = 0                                           # inicializa o contador de divisores do número
    for pd in range(1, x+1):                                    # percorre todos os números de 1 até x
        if x % pd == 0:                                         # verifica se a divisão de x por pd possui resto zero
            qtd_divisores += 1                                  # aumenta o contador quando encontra um divisor
    return qtd_divisores == 2                                   # retorna True se o número possuir exatamente dois divisores

def main():                                                 # define a função principal do programa
    nao_primos = []                                             # cria uma lista vazia para armazenar os números não primos
    primos = []                                                 # cria uma lista vazia para armazenar os números primos
    n = int(input())                                            # solicita a quantidade de números que serão digitados e converte para inteiro
    for i in range(n):                                          # repete o bloco de código n vezes
        x = int(input())                                        # solicita um número ao usuário e converte para inteiro
        if eh_primo(x):                                         # chama a função e verifica se o número é primo
            primos.append(x)                                    # adiciona o número ao final da lista de primos
        else:                                                   # executa caso o número não seja primo
            nao_primos.append(x)                                # adiciona o número ao final da lista de não primos
    print(f'Lista de numeros primos: {primos}')                 # exibe a lista de números primos
    print(f'Lista de numeros não primos: {nao_primos}')         # exibe a lista de números não primos


if __name__ == "__main__":                                  # verifica se o arquivo está sendo executado diretamente
    main()                                                  # chama a função principal do programa