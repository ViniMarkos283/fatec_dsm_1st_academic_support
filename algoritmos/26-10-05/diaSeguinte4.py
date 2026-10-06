'''
    Crie um programa que solicite ao usuario uma data
    no formato dd/mm/aaaa e exiba a data do dia seguinte.

    Caso a data não seja valida, exiba uma mensagem indicativa.

    OBS: considere como validos os anos a partir de 1900.

    [Upgrade 1]: Permita que o usuario visualize não apenas
    o dia seguinte, mas tambem o dia anterior.

    [Upgrade 2]: permita que o programa tambem exiba dois dias a frente.

    [Upgrade 3]: permita q o programa exiba diversas datas posteriores e anterioes a data
    que o usuario inserir. Quem escolherá quantos dias antes e depois será o próprio usuario

'''

def data_valida(d:int,m:int,a:int) -> bool:                     # função que verifica se a data é um valor valido
    if a < 1900:                                                    # se a data for menor que 1900...
        return False                                                # ...devolve a data como invalida
    if m < 1 or m > 12:                                             # se o mes for menor que 1 (janeiro) ou maior que 12 (dezembro)...
        return False                                                # ...devolve como invalido
    if d >= 1 and d <= dia_maximo(m, a):                            # se o dia for mais ou igual a 1 e tambem for igual ou menor q o dia maximo daquele mes...
        return True                                                 # ...devolve a data como verdadeira
    else:                                                           # se o dia não atender a condição acima...
        return False                                                # ...devolve a data como invalida

def dia_maximo(m:int, a:int) -> int:                            # função que confere o dia maximo do mes informado
    if m == 2:                                                      # se o mes for fevereiro...
        return 28 + bissexto(a)                                     # ...devolvemos 28 junto a confirmação se o ano é ou não bisssexto (0 ou 1)
    elif m == 4 or m == 6 or m == 9 or m == 11:                     # ou se, caso o mes acabe com 30 dias...
        return 30                                                   # ...devolve 30
    else:                                                           # senão...
        return 31                                                   # ...devolvemos 31

def bissexto(a:int) -> bool:                                    # função que confere se o ano é bissexto ou não
    if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):               # se o ano for divivisel por 400 (resto zero) e a divisão por 100 nãp tiver resto zero...
        return True                                                 # ...devolvemos verdadeiro, o ano é bissexto
    else:                                                           # senão...
        return False                                                # ...devolvemos falso, logo o ano não é bissexto

# [Upgrade 1 - edição lucio, usando lista]
def exibe_da(d:int,m:int,a:int) -> list:                        # função que exibe o dia anterior ao informado
    if d-1 < 1:                                                     # se o dia anterior foi menor q o dia 1...
        d = dia_maximo(m-1,a)                                       # ...o dia anterior será o dia maximo do mes anterior
        m -= 1                                                      # e voltamos um mes
    else:                                                           # senao...
        d -= 1                                                      # ...só tiramos um dia
    if m < 1:                                                       # se o mes for menor que janeiro...
        m = 12                                                      # ...ele passará a ser dezembro
        a -= 1                                                      # e voltamos um ano
    return [d,m,a]

# [Upgrade 2 - edição lucio, usando lista]
def exibe_ds(d:int,m:int,a:int) -> list:                        # função que exibe o dia seguinte ao que foi informado
    if d+1 > dia_maximo(m, a):                                      # se o dia seguinte foi maior q o dia maximo daquele mes...
        d = 1                                                       # o proximo dia é o primeiro dia do mes
        m += 1                                                      # e passamos pro mes seguinte
    else:                                                           # senão...
        d += 1                                                      # ...só passamos pro dia seguinte
    if m > 12:                                                      # se o mes ultrapassar dezembro...
        m = 1                                                       # ...o mes seguinte será janeiro
        a += 1                                                      # e passamos pro proximo ano
    return [d,m,a]

def main():                                                     # função inicial, a que chama as outras e resolve o problema principal
    d, m, a= map(int, input('Data? ').split('/'))                   # pediremos ao usuario q digite uma data no formato dd/mm/aaaa, e depois convertemos para int e dividimos os valores nas variaveis d, m e a, usando o / como parametro de divisão
    if data_valida(d,m,a):                                          # checaremos se a data é valida, chamando a função responsavel pela conferencia, se a função devolver verdadeiro...

# ------ quantia de dias posteriores -------

        x,y,z = d,m,a                                               # passamos dia, mes e ano para z, y e z
        qtd_dps = int(input('Quantos dias depois? '))               # pedimos q o usuario digite a quantia de dias posteriores a data

        i = 0                                                       # inicializa o I zerado
        while i < qtd_dps:                                          # enquanto o valor de I for menor que a quantia de dias posteriores...
            x,y,z = exibe_ds(d,m,a)                                 # x, y e z recebem o valor devolvido da função exibe_ds
            print(f'dia seguinte: {x:02}/{y:02}/{z}')               # imprimimos o valor obtido da função
            i += 1                                                  # acrescemos 1 ao valor do I

# ------ quantia de dias anteriores -------
        x,y,z = d,m,a                                               # passamos dia, mes e ano para z, y e z
        qtd_ant = int(input('Quantos dias antes? '))                # pedimos q o usuario digite a quantia de dias anteriores a data

        i = 0                                                       # inicializa o I zerado
        while i < qtd_ant:                                          # enquanto o valor de I for menor que a quantia de dias anteriores...
            x,y,z = exibe_da(d,m,a)                                 # x, y e z recebem o valor devolvido da função exibe_ds
            print(f'dia anterior: {x:02}/{y:02}/{z}')               # imprimimos o valor obtido da função
            i += 1                                                  # acrescemos 1 ao valor do I
    else:                                                           # se a função que confere a data devolver falso...
        print('Data invalida!')                                     # ...imprimimos que a data é invalida

main()                                                          # inicializa o script, chamando a função main

# [ need fix yet ]
