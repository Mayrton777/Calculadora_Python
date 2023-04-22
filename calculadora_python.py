import math

#função operadores
def soma(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mult(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2
def expo(num1, num2):
    return num1 ** num2
def raiz(num1):
    return math.sqrt(num1)

operacoes = {
    '+': soma,
    '-': sub,
    '*': mult,
    '/': div,
    '**': expo,
    'raiz': raiz,
}

print("Calculadora Python")

#loop
while True:
    try:
        #Entrada num1
        num1 = input("Digite o primeiro número ou 'q' para sair: ")

        #Condição para sair do loop
        if num1 == 'q':
            break

        num1 = float(num1)
        #Entrada operador
        operador = input("Digite o operador '+, -, *, /, **, raiz': ")

        if operador not in operacoes:
            print("Operador inválido!")
            continue

        if operador == 'raiz':
            resultado = operacoes[operador](num1)
            print("A raiz de {} é {:.2f}".format(num1,resultado))
            continue

        #Entrada num2
        num2 = float(input("Digite o segundo número: "))

        #Resultado
        resultado = operacoes[operador](num1,num2)
        print("O resultado é: {:.2f}".format(resultado))

    except ValueError:
        print("Valor inválido! Por favor, digite um valor válido.")