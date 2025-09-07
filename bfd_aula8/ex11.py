vendedores = ['João', 'Maria', 'Pedro', 'Ana']

print("=== Ranking de Vendas ===")
for posicao, vendedor in enumerate(vendedores, start=1):
    print(f"{posicao}. {vendedor}")
