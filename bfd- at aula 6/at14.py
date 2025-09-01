senha_correta = "python123"

senha_digitada = input("Digite a senha: ")

while senha_digitada != senha_correta:
    print("Senha incorreta. Tente novamente.")
    senha_digitada = input("Digite a senha: ")

print("Acesso permitido! Senha correta.")
