import tkinter as tk
import operacoes

OPERACOES_DISPONIVEIS = {
    '+': operacoes.soma,
    '-': operacoes.sub,
    '*': operacoes.mult,
    '/': operacoes.div,
    '**': operacoes.expo,
    'raiz': operacoes.raiz,
}

#Função do cálculo
def calcular():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        operador = operador_entry.get()

        if operador not in OPERACOES_DISPONIVEIS:
            resultado_label.configure(text="Operador inválido!")
            return
              
        resultado = OPERACOES_DISPONIVEIS[operador](num1,num2)
        resultado_label.configure(text="O resultado é: {:.2f}".format(resultado))

    except ValueError:
        resultado_label.configure(text="Valor inválido! Por favor, digite um número válido.")

#Função para calcular a raiz
def calcular_raiz():
    try:
        num1 = float(num1_entry.get())
        resultado = OPERACOES_DISPONIVEIS['raiz'](num1)
        resultado_label.configure(text="A raiz quadrade de {} é {:.2f}".format(num1, resultado))
    except ValueError:
        resultado_label.config(text="Valor inválido! Por favor, digite um número válido.")

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
raiz_button = tk.Button(janela, text="Raiz", command=calcular_raiz)
resultado_label = tk.Label(janela, text="Resultado:")

#Posição widgets
num1_label.grid(row=0, column=0)
num1_entry.grid(row=0, column=1)
operador_label.grid(row=1, column=0)
operador_entry.grid(row=1, column=1)
num2_label.grid(row=2, column=0)
num2_entry.grid(row=2, column=1)
calcular_button.grid(row=3, column=0, columnspan=2)
raiz_button.grid(row=3, column=1, columnspan=2)
resultado_label.grid(row=4, column=0, columnspan=2)

 #inicia o loop principal da janela
janela.mainloop()