def responsavel(feedback:int) -> str:               # define uma função que recebe um número inteiro e retorna uma string
    match feedback:                                     # compara o valor de feedback com os casos definidos abaixo
        case 1: return 'Rolien'                         # se feedback for 1, retorna o nome Rolien
        case 2: return 'Naej'                           # se feedback for 2, retorna o nome Naej
        case 3: return 'Elehcim'                        # se feedback for 3, retorna o nome Elehcim
        case _: return 'Odranoel'                       # caso nenhum dos anteriores corresponda, retorna Odranoel

def main():                                         # define a função principal do programa
    qtd_dias = int(input())                             # solicita a quantidade de dias e converte o valor para inteiro
    for i in range(qtd_dias):                           # repete o bloco de código uma vez para cada dia
        qtd_feedbacks = int(input())                    # solicita a quantidade de feedbacks recebidos no dia atual
        for j in range(qtd_feedbacks):                  # repete o bloco de código para cada feedback do dia
            feedback = int(input())                     # solicita o código do feedback e converte para inteiro
            print(responsavel(feedback))                # chama a função responsavel e exibe o nome correspondente ao feedback


if __name__ == '__main__':                          # verifica se o arquivo está sendo executado diretamente
    main()                                          # chama a função principal do programa