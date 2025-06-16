import tkinter as tk
from math import *

# Função para avaliar a expressão
def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao, {"__builtins__": None}, {
            "sqrt": sqrt, "sin": sin, "cos": cos, "tan": tan,
            "log": log, "log10": log10, "factorial": factorial,
            "pi": pi, "e": e, "pow": pow
        })
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

# Função para adicionar texto no campo de entrada
def adicionar(valor):
    entrada.insert(tk.END, valor)

# Função para limpar a entrada
def limpar():
    entrada.delete(0, tk.END)

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora Científica")
janela.geometry("400x500")
janela.resizable(False, False)

# Campo de entrada
entrada = tk.Entry(janela, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entrada.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=10)

# Botões
botoes = [
    ["7", "8", "9", "/", "sqrt"],
    ["4", "5", "6", "*", "log10"],
    ["1", "2", "3", "-", "log"],
    ["0", ".", "(", ")", "+"],
    ["sin", "cos", "tan", "pow", "**"],
    ["pi", "e", "factorial", "C", "="]
]

# Criar os botões na interface
for linha in botoes:
    frame = tk.Frame(janela)
    frame.pack(expand=True, fill="both")
    for texto in linha:
        if texto == "=":
            botao = tk.Button(frame, text=texto, font=("Arial", 16), command=calcular)
        elif texto == "C":
            botao = tk.Button(frame, text=texto, font=("Arial", 16), command=limpar)
        else:
            botao = tk.Button(frame, text=texto, font=("Arial", 16),
                              command=lambda t=texto: adicionar(t))
        botao.pack(side=tk.LEFT, expand=True, fill="both")

# Rodar o aplicativo
janela.mainloop()
