numeros = [10, 20, 30, 40, 50]

variavel_temporaria = 0  
soma = 0 


while variavel_temporaria < len(numeros):
    soma += numeros[variavel_temporaria]
    variavel_temporaria += 1  

print("A soma dos elementos da lista é:", soma)
