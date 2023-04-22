import tkinter as tk
import math

#Funções
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

#Função do cálculo
def calcular():
    try:
        num1 = float(num1_entry.get())
        operador = operador_entry.get()

        if operador not in operacoes:
            resultado_label.configure(text="Operador inválido!")
            return

        #raiz
        if operador == 'raiz':
            resultado = operacoes[operador](num1)
            resultado_label.configure(text="A raiz quadrada de {} é {:.2f}".format(num1,resultado))

        num2 = float(num2_entry.get())
                     
        resultado = operacoes[operador](num1,num2)
        resultado_label.configure(text="O resultado é: {:.2f}".format(resultado))

    except ValueError:
        resultado_label.configure(text="Valor inválido! Por favor, digite um número válido.")

#Interface gráfica
janela = tk.Tk()
janela.title("Calculadora Python")

#Widgets
num1_label = tk.Label(janela, text="Primeiro número:")
num1_entry = tk.Entry(janela)
operador_label = tk.Label(janela, text="Operador:")
operador_entry = tk.Entry(janela)
num2_label = tk.Label(janela, text="Segundo número:")
num2_entry = tk.Entry(janela)
calcular_button = tk.Button(janela, text="Calcular", command=calcular)
resultado_label = tk.Label(janela, text="Resultado:")

#Posição widgets
num1_label.grid(row=0, column=0)
num1_entry.grid(row=0, column=1)
operador_label.grid(row=1, column=0)
operador_entry.grid(row=1, column=1)
num2_label.grid(row=2, column=0)
num2_entry.grid(row=2, column=1)
calcular_button.grid(row=3, column=0, columnspan=2)
resultado_label.grid(row=4, column=0, columnspan=2)

#inicia o loop principal da janela
janela.mainloop()