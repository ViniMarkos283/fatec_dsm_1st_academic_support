def eh_primo(x:int) -> bool:
    qtd_divisores = 0
    for pd in range(1, x+1):
        if x % pd == 0:
            qtd_divisores += 1
    return qtd_divisores == 2

def main():
    n = int(input())
    for i in range(n):
        x = int(input())
        if eh_primo(x):
            print(f'{x} eh primo')
        else:
            print(f'{x} nao eh primo')

if __name__ == "__main__":
    main()
