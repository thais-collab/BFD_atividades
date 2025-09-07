def buscar_livro(titulo, **kwargs):
    print("=== Busca de Livro ===")
    print(f"Título: {titulo}")
    if kwargs:
        print("Filtros aplicados:")
        for chave, valor in kwargs.items():
            print(f"- {chave.capitalize()}: {valor}")

buscar_livro(
    "Dom Casmurro",
    autor="Machado de Assis",
    ano=1899,
    gênero="Romance"
)
