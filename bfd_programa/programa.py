def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b
try:
  
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /): ")

    if operacao == "+":
        resultado = soma(num1, num2)
    elif operacao == "-":
        resultado = subtracao(num1, num2)
    elif operacao == "*":
        resultado = multiplicacao(num1, num2)
    elif operacao == "/":
        if num2 == 0:
            raise ZeroDivisionError
        resultado = divisao(num1, num2)
    else:
        raise ValueError("operação inválida")

except ValueError as e:
    if str(e) == "operação inválida":
        print("Erro: operação inválida")
    else:
        print("Erro: valor inválido")

except ZeroDivisionError:
    print("Erro: divisão por zero")

else:
    print("Resultado:", resultado)

finally:
    print("Fim do programa")
