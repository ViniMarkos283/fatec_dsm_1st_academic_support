def salario_bruto(vh:float, qtd_horas:int) -> float:                # define uma função que recebe o valor da hora e a quantidade de horas, retornando um número decimal
    return vh * qtd_horas                                               # multiplica o valor da hora pela quantidade de horas e retorna o salário bruto

def vale_transporte(sb:float) -> float:                             # define uma função que recebe o salário bruto e retorna o valor do vale-transporte
    return sb * 0.06                                                    # calcula 6% do salário bruto

def irrf(sb:float) -> float:                                        # define uma função que recebe o salário bruto e retorna o valor do imposto de renda
    return sb * 0.15                                                    # calcula 15% do salário bruto

def salario_liquido(sb: float, vt:float, imposto:float) -> float:   # define uma função que recebe o salário bruto, o vale-transporte e o imposto
    return sb - vt - imposto                                            # subtrai os descontos do salário bruto e retorna o salário líquido

def main():                                                         # define a função principal do programa
    print('Testes das funções criadas')                                 # exibe uma mensagem indicando que os testes serão iniciados
    sb = salario_bruto(10, 200)                                         # chama a função salario_bruto com valor da hora 10 e 200 horas trabalhadas
    vt = vale_transporte(sb)                                            # calcula o vale-transporte com base no salário bruto
    imposto = irrf(sb)                                                  # calcula o imposto de renda com base no salário bruto
    print(sb, vt, imposto)                                              # exibe os valores do salário bruto, vale-transporte e imposto
    sl = salario_liquido(sb,vt,imposto)                                 # calcula o salário líquido utilizando os valores anteriores
    print(sl)                                                           # exibe o resultado do salário líquido


if __name__ == '__main__':                                          # verifica se o arquivo está sendo executado diretamente, e não importado por outro arquivo
    main()                                                          # chama a função principal do programa

"""
    __name__ -> variável especial do Python que armazena o nome do módulo.

    quando o arquivo é executado diretamente, recebe a string "__main__".

    quando o arquivo é importado por outro módulo, recebe o nome do próprio arquivo.

    boa prática: utilizar esse if para evitar que a função main() seja executada
    automaticamente quando o arquivo for importado.
"""