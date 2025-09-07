
def cadastrar_usuario(nome, email, **kwargs):
    print("=== Ficha de Cadastro ===")
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    for chave, valor in kwargs.items():
        print(f"{chave.capitalize()}: {valor}")


cadastrar_usuario(
    nome="Ana",
    email="ana@email.com",
    idade=30,
    cidade="Salvador",
    profissão="Engenheira"
)
