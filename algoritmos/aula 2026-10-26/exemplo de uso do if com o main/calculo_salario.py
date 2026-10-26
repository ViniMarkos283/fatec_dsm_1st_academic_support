from calculos_trabalhistas import *

def main():
    vh = float(input('valor das horas: '))
    qtd_horas = int(input('quantidade de horas: '))
    sb = salario_bruto(vh, qtd_horas)
    print(f'Seu salario bruto é R$ {sb:.2f}')
    vt = vale_transporte(sb)
    print(f'Valor do VT é de R${vt:.2f}')
    imposto = irrf(sb)
    print(f'Valor do IRRF é R$ {imposto:.2f}')
    sl = salario_liquido(sb, vt, imposto)
    print(f'Salario liquido R$ {sl:.2f}')

main()
