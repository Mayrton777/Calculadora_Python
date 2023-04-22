import tkinter as tk
from tkinter import messagebox
import operacoes
import sys

# Dicionário com as operações disponíveis
OPERACOES_DISPONIVEIS = {
    '+': operacoes.soma,
    '-': operacoes.sub,
    '*': operacoes.mult,
    '/': operacoes.div,
    '**': operacoes.expo,
    'raiz': operacoes.raiz,
}

# Função que obtem os valores digitados nos campos e realiza validações
def obter_valores():
    """
    Obtém os valores digitados nos campos e realiza validações.

    Raises:
        ValueError: se algum valor digitado não for um número válido ou se o operador não for válido.

    Returns:
        tuple: um tuple contendo os valores numéricos e o operador.
    """
    num1_text = num1_entry.get()
    num2_text = num2_entry.get()
    operador = operador_entry.get()
    try:
        num1 = float(num1_text)
        num2 = float(num2_text)
    except ValueError:
        raise ValueError("Valores inválidos! Por favor, digite números válidos.")
    if operador not in OPERACOES_DISPONIVEIS:
        raise ValueError("Operador inválido! Por favor, digite um dos seguintes operadores: +, -, *, / ou **")
    if operador == '/' and num2 == 0:
        raise ValueError("Divisão por zero!")
    return num1, num2, operador

# Função que realiza a operação escolhida
def calcular_operacao(num1, num2, operador):
    """
    Realiza a operação escolhida.

    Args:
        num1 (float): o primeiro número da operação.
        num2 (float): o segundo número da operação.
        operador (str): o operador da operação.

    Raises:
        ValueError: se o operador não for válido.

    Returns:
        float: o resultado da operação.
    """
    if operador == 'raiz':
        return OPERACOES_DISPONIVEIS[operador](num1)
    return OPERACOES_DISPONIVEIS[operador](num1, num2)

#Função do cálculo
def calcular():
    try:
        num1, num2, operador = obter_valores()
        resultado = calcular_operacao(num1, num2, operador)
        resultado_label.configure(text=f"O resultado é: {resultado:.2f}")
    except ValueError as e:
        tk.messagebox.showerror("Erro", str(e))
    except ZeroDivisionError as e:
        # Verifica qual é o erro específico que ocorreu
        e = sys.exc_info()[1]
        if "Valor invalido" in str(e):
            tk.messagebox.showerror("Erro","Valor inválido! Por favor digite um número válido.")
        elif "Divisão por zero" in str(e):
            tk.messagebox.showerror("Erro","Divisão por zero!")
        elif "Operador invalido" in str(e):
            tk.messagebox.showerror("Erro","Operador inválido!")
        else:
            tk.messagebox.showerror("Erro","Erro desconhecido")

# Função que é executada quando o botão 'Raiz' é pressionado
def calcular_raiz():
    try:
        num1 = float(num1_entry.get())
        resultado = operacoes.raiz(num1)
        resultado_label.configure(text=f"A raiz quadrade de {num1} é {resultado:.2f}")
    except ValueError:
        tk.messagebox.showerror("Erro","Valor inválido! Por favor, digite um número válido.")

# Cria uma nova janela
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

#Posição dos widgets na janela
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