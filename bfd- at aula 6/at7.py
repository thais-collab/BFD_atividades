status = input("Digite o status do pedido (recebido, em_preparacao, em_entrega, entregue): ")

match status:
    case "recebido":
        print("Seu pedido foi recebido e está sendo processado.")
    case "em_preparacao":
        print("Seu pedido está em preparação.")
    case "em_entrega":
        print("Seu pedido saiu para entrega.")
    case "entregue":
        print("Pedido entregue com sucesso! Obrigado pela preferência.")
    case _:
        print("Status não identificado. Verifique e tente novamente.")
