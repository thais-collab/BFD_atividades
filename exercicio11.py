dias = int(input("Quantos dias o carro foi alugado?"))
km = float(input("Quantos km foram percorridos?"))
preco_dias = dias * 60
preco_km = km * 0.15
total = preco_dias + preco_km
print("O preço total a pagar é R$", total)