def responsavel(feedback:int) -> str:
    match feedback:
        case 1: return 'Rolien'
        case 2: return 'Naej'
        case 3: return 'Elehcim'
        case _: return 'Odranoel'

def main():
    qtd_dias = int(input())
    for i in range(qtd_dias):
        qtd_feedbacks = int(input())
        for j in range(qtd_feedbacks):
            feedback = int(input())
            print(responsavel(feedback))


if __name__ == '__main__':
    main()
