print("Calculadora Python")

while True:
    try:
        #Entrada num1
        num1 = input("Digite o primeiro número ou 'q' para sair: ")

        #Condição para sair do loop
        if num1 == 'q':
            break

        num1 = float(num1)
        #Entrada operador e num2
        operador = input("Digite o operador '+, -, *, /, **, %': ")
        num2 = float(input("Digite o segundo número: "))

        #Operadores
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            resultado = num1 / num2
        elif operador == '**':
            resultado = num1 / num2
        elif operador == '%':
            resultado = num1 % num2
        else:
            print("Operador invalido")
            resultado = None

        #Resultado
        if resultado is not None:
            print("O resultado é: {:.2f}".format(resultado))
    except ValueError:
        print("Valor inválido! Por favor, digite um valor válido.")