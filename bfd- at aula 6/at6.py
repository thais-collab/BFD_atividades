nota = int(input("Digite uma nota de 1 a 5: "))
match nota:
    case 1:
        print("Muito ruim! Precisa melhorar bastante.")
    case 2:
        print("Ruim! Continue praticando.")
    case 3:
        print("Regular! Você pode melhorar.")
    case 4:
        print("Bom! Está quase perfeito.")
    case 5:
        print("Excelente! Parabéns pelo desempenho.")
    case _:
        print("Erro: nota inválida! Digite um valor entre 1 e 5.")
