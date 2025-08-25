produtos = ['Arroz', 'macarrão', 'açucar', 'feiijão', 'batata']
print(produtos [1:4])

#append é utilizado para adicionar produtos a lista.
print(produtos)
produtos.append('chocolate')
print(produtos)

# insert se usa para colocar um produto na posição que vocÊ desejar.
produtos.insert(0, "sorvete")
print(produtos)


# remove é utilizado para remover produtos da lista 
#print(produtos)
#produtos.remove ([])
#print(produtos)

# coloca a lista em ordem alfabetica
produtos.sort()
print(produtos)

# coloca a lista ao contrario da ordem alfabetica ex. c,b,a
produtos.reverse()
print(produtos)

# conta quanto de um produto especifico tem na lista ex: quantos arroz
print(produtos.count("Arroz"))

# mostra a posição do produto na lista
print(produtos.index("açucar"))

# o len conta quantos produtos tem na lista
print(len(produtos))

# o del é usado para apagar definitivamente um item da lista
print(produtos)
del produtos[0]
print(produtos)

# o clear é utilizado para apagar todos os itens da lista
produtos.clear()
print(produtos)

# tupla 
modelo_carro = ()
modelo_carro = ("Toyota","Corolla", "2025")
print(modelo_carro[0:2])
