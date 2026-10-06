'''
    Crie um programa que solicite ao usuario uma data
    no formato dd/mm/aaaa e exiba a data do dia seguinte.

    Caso a data não seja valida, exiba uma mensagem indicativa.

    OBS: considere como validos os anos a partir de 1900.

    [Upgrade 1]: Permita que o usuario visualize não apenas
    o dia seguinte, mas tambem o dia anterior.

    [Upgrade 2]: permita que o programa tambem exiba dois dias a frente.

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

def exibe_ds(d:int,m:int,a:int):                                # função que exibe o dia seguinte ao que foi informado
    if d+1 > dia_maximo(m, a):                                      # se o dia seguinte foi maior q o dia maximo daquele mes...
        d = 1                                                       # o proximo dia é o primeiro dia do mes
        m += 1                                                      # e passamos pro mes seguinte
    else:                                                           # senão...
        d += 1                                                      # ...só passamos pro dia seguinte
    if m > 12:                                                      # se o mes ultrapassar dezembro...
        m = 1                                                       # ...o mes seguinte será janeiro
        a += 1                                                      # e passamos pro proximo ano
    print(f'dia seguinte: {d}/{m}/{a}')                             # imprimimos a data obtida

# [Upgrade 1]
def exibe_da(d:int,m:int,a:int):                                # função que exibe o dia anterior ao informado
    if d-1 < 1:                                                     # se o dia anterior foi menor q o dia 1...
        d = dia_maximo(m-1,a)                                       # ...o dia anterior será o dia maximo do mes anterior
        m -= 1                                                      # e voltamos um mes
    else:                                                           # senao...
        d -= 1                                                      # ...só tiramos um dia
    if m < 1:                                                       # se o mes for menor que janeiro...
        m = 12                                                      # ...ele passará a ser dezembro
        a -= 1                                                      # e voltamos um ano
    print(f'dia anterior: {d}/{m}/{a}')                             # imprimimos a data obtida

# [Upgrade 2]
def exibe_dps_a(d:int,m:int,a:int):                             # função que exibe dois dias depois da data informada
    if d+2 > dia_maximo(m, a):                                      # se depois de amanha ultrapassar o dia maximo do mes...
        d = d + 2 - dia_maximo(m, a)                                # ...o dia passará a ser ele, acrescido de 2 menos o mes inteiro
        m += 1                                                      # e passamos de mes
    else:                                                           # senao...
        d += 2                                                      # ...só passamos 2 dias
    if m > 12:                                                      # se o mes passar de dezembro...
        m = 1                                                       # ...o mes passará a ser janeiro
        a += 1                                                      # e passamos de ano
    print(f'dois dias depois: {d}/{m}/{a}')                         # imprimimos a data obtida

# [Upgrade 2 - edição lucio, usando lista]
def exibe_ds2(d:int,m:int,a:int):                                # função que exibe o dia seguinte ao que foi informado, mas com lista
    if d+1 > dia_maximo(m, a):                                      # se o dia seguinte foi maior q o dia maximo daquele mes...
        d = 1                                                       # o proximo dia é o primeiro dia do mes
        m += 1                                                      # e passamos pro mes seguinte
    else:                                                           # senão...
        d += 1                                                      # ...só passamos pro dia seguinte
    if m > 12:                                                      # se o mes ultrapassar dezembro...
        m = 1                                                       # ...o mes seguinte será janeiro
        a += 1                                                      # e passamos pro proximo ano
    return [d,m,a]                                                  # devolvemos os 3 valores dentro da lista

def main():                                                     # função inicial, a que chama as outras e resolve o problema principal
    d, m, a= map(int, input('Data? ').split('/'))                   # pediremos ao usuario q digite uma data no formato dd/mm/aaaa, e depois convertemos para int e dividimos os valores nas variaveis d, m e a, usando o / como parametro de divisão
    if data_valida(d,m,a):                                          # checaremos se a data é valida, chamando a função responsavel pela conferencia, se a função devolver verdadeiro...
        exibe_ds(d,m,a)                                             # ...chamaremos as seguintes funções respectivamente: a que exibe o dia seguinte, a que exibe o dia anterior e a que exibe a data 2 dias depois
        exibe_da(d,m,a)
        exibe_dps_a(d,m,a)

        x,y,z = d,m,a                                               # passamos o dia, mes e ano para as variaveis x, y e z
        i = 0                                                       # inicializa a variavel I zerada
        while i < 10:                                               # enquanto o valor de I não ultrapassar 10...
            x,y,z = exibe_ds2(d,m,a)                                # os valores x, y e z recebem o retorno da função exbie_ds2
            print(f'dia seguinte: {x:02}/{y:02}/{z}')               # imprimimos o valor obtido da função
            i += 1                                                  # acrescemos o I de 1
    else:                                                           # se a função que confere a data devolver falso...
        print('Data invalida!')                                     # ...imprimimos que a data é invalida

main()                                                          # inicializa o script, chamando a função main
