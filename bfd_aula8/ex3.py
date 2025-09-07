def contar_vogais(texto):
    vogais = "aeiouAEIOU" 
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

entrada = "O show do system é um sonho!"
resultado = contar_vogais(entrada)

print("Texto:", entrada)
print("Quantidade de vogais:", resultado)
