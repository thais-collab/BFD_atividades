numero = int(input("Digite o numero que você quer a tabuada: "))

print(f"\nTabuada do {numero}:")
for i in range(1, 11):  
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
