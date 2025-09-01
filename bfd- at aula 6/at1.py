# Passo 01
IDADE_MINIMA = 18
# Recebendo a idade do usuário
idade_usuario = int(input("Digite sua idade: "))

# Passo 01 + Passo 02 + Passo 03
if idade_usuario >= IDADE_MINIMA:
    print("O usuário é maior de idade.")
elif idade_usuario >= 16:  
    print("O usuário é menor e tem 16 ou 17 anos.")
else:
    print("O usuário é menor de idade.")
