def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador


entrada = "Hoje irei para a pista de ciclismo!"
resultado = contar_vogais(entrada)

print("Texto:", entrada)
print("Quantidade de vogais:", resultado)
