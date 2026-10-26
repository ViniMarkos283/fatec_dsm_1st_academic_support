'''
    Crie um programa que solicite ao usuario uma quantidade
    positiva de numeros e, em seguida, os n numeros.
    O programa deverá, ao final, exibir duas listas, uma
    com os primos digitados e a outra com os não primos.
'''

def eh_primo(x:int) -> bool:
    qtd_divisores = 0
    for pd in range(1, x+1):
        if x % pd == 0:
            qtd_divisores += 1
    return qtd_divisores == 2

def main():
    nao_primos = []
    primos = []
    n = int(input())
    for i in range(n):
        x = int(input())
        if eh_primo(x):
            primos.append(x)
        else:
            nao_primos.append(x)
    print(f'Lista de numeros primos: {primos}')
    print(f'Lista de numeros não primos: {nao_primos}')


if __name__ == "__main__":
    main()
