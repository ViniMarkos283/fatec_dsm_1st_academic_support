def eh_primo(x:int) -> bool:                # define uma função que recebe um inteiro e retorna True ou False
    qtd_divisores = 0                           # inicializa o contador de divisores do número
    for pd in range(1, x+1):                    # percorre todos os números de 1 até x
        if x % pd == 0:                         # verifica se a divisão de x por pd possui resto zero
            qtd_divisores += 1                  # aumenta o contador quando encontra um divisor
    return qtd_divisores == 2                   # retorna True se o número possuir exatamente dois divisores

def main():                                 # define a função principal do programa
    n = int(input())                            # solicita a quantidade de números que serão verificados e converte para inteiro
    for i in range(n):                          # repete o bloco de código n vezes
        x = int(input())                        # solicita um número ao usuário e converte para inteiro
        if eh_primo(x):                         # chama a função e verifica se o número é primo
            print(f'{x} eh primo')              # exibe que o número é primo
        else:                                   # executa caso a função retorne False
            print(f'{x} nao eh primo')          # exibe que o número não é primo

if __name__ == "__main__":                  # verifica se o arquivo está sendo executado diretamente
    main()                                  # chama a função principal do programa