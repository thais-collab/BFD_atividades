def calcular_media(*args):
    if len(args) == 0:
        return 0  
    return round(sum(args) / len(args), 2)  

resultado = calcular_media(8.5, 9.0, 7.5)
print("Média das notas:", resultado)
