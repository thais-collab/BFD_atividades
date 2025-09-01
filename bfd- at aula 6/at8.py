cor = input("Digite a cor do semáforo (verde, amarelo, vermelho): ").lower()

match cor:
    case "verde":
        print("Siga em frente.")
    case "amarelo":
        print("Atenção! Prepare-se para parar.")
    case "vermelho":
        print("Pare o veículo.")
    case _:
        print("Sinal inválido. Digite apenas verde, amarelo ou vermelho.")
