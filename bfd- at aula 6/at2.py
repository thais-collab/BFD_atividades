# Passo 01: 
NOTA_MINIMA = 7.0
nota_final = float(input("Digite a sua nota final: "))

# Passo 01 + Passo 02 + Passo 03
if nota_final >= NOTA_MINIMA:
    print("Aprovado!")
elif nota_final >= 5.0: 
    print("Você não foi muito bem. Mas ainda consegue recuperar.")
else:
    print("Reprovado!")
