def salario_bruto(vh:float, qtd_horas:int) -> float:
    return vh * qtd_horas

def vale_transporte(sb:float) -> float:
    return sb * 0.06

def irrf(sb:float) -> float:
    return sb * 0.15

def salario_liquido(sb: float, vt:float, imposto:float) -> float:
    return sb - vt - imposto

def main():
    print('Testes das funções criadas')
    sb = salario_bruto(10, 200)
    vt = vale_transporte(sb)
    imposto = irrf(sb)
    print(sb, vt, imposto)
    sl = salario_liquido(sb,vt,imposto)
    print(sl)


if __name__ == '__main__':
    main()

"""
    __name__ -> guarda o nome do arquivo quando importado.
    
    quando carregado diretamente pelo F5, guardará a str "__main__"

    boas praticas: colocar esse if em todo script python

"""
