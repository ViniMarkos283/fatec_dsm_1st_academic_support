from calculos_trabalhistas import *                     # importa todas as funções e definições do módulo calculos_trabalhistas

def main():                                             # define a função principal do programa
    vh = float(input('valor das horas: '))              # solicita o valor de cada hora trabalhada e converte para número decimal
    qtd_horas = int(input('quantidade de horas: '))     # solicita a quantidade de horas trabalhadas e converte para inteiro
    sb = salario_bruto(vh, qtd_horas)                   # chama a função salario_bruto e armazena o resultado na variável sb
    print(f'Seu salario bruto é R$ {sb:.2f}')           # exibe o salário bruto com duas casas decimais
    vt = vale_transporte(sb)                            # calcula o valor do vale-transporte com base no salário bruto
    print(f'Valor do VT é de R${vt:.2f}')               # exibe o valor do vale-transporte com duas casas decimais
    imposto = irrf(sb)                                  # calcula o imposto de renda retido na fonte (IRRF) com base no salário bruto
    print(f'Valor do IRRF é R$ {imposto:.2f}')          # exibe o valor do imposto com duas casas decimais
    sl = salario_liquido(sb, vt, imposto)               # calcula o salário líquido descontando VT e IRRF do salário bruto
    print(f'Salario liquido R$ {sl:.2f}')               # exibe o salário líquido com duas casas decimais

main()                                                  # chama a função principal do programa