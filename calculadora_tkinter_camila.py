"""
Resumo do codigo:

No código, uma calculadora é criada usando a biblioteca Tkinter do Python. 
A interface gráfica consiste em uma janela com três seções:

TOPO, MEIO E BAIXO 

A seção TOPO exibe o histórico das operações, 
A seção MEIO mostra o resultado das operações.
Na seção BAIXO são exibidos botões com os números
e os símbolos das operações possíveis, o "=" 
e o botão C (clear).

Ao clicar nesses botões os caracteres são adicionados à área de exibição. 
O botão "=" realiza o cálculo da expressão e exibe o resultado. 
Há também um botão para limpar a calculadora, o "C".

"""

import tkinter as tk
from tkinter import *

janela = Tk()

janela.title("Calculadora com Tkinter")
#janela.resizable(width=FALSE,height=FALSE)

def adicionar_caractere(caractere):
    display.insert(tk.END, caractere)

def calcular():
    expressao = display.get()
    try:
        resultado = eval(expressao)
        display.delete(0, tk.END)
        display.insert(tk.END, str(resultado))
        historico.config(text=expressao + " =")
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Erro")
        historico.config(text="")

def limpar():
    display.delete(0, tk.END)
    historico.config(text="")

# Definir proporções
janela.columnconfigure(0, weight=15, minsize=5)  # Topo
janela.columnconfigure(1, weight=15, minsize=5)  # Meio
janela.columnconfigure(2, weight=15, minsize=5)  # Baixo

# Seção do topo
historico = tk.Label(janela, text="", anchor="e")
historico.grid(row=0, column=0, columnspan=3, sticky="nsew")

# Seção do meio
display = tk.Entry(janela, width=30, justify="right")
display.grid(row=1, column=0, columnspan=3, sticky="nsew")

# Seção do baixo
botoes = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 2
col = 0
for botao in botoes:
    if botao == "=":
        tk.Button(janela, text=botao, width=10, command=calcular).grid(row=row, column=col, columnspan=2, sticky="nsew")
        col += 1
    elif botao == "0":
        tk.Button(janela, text=botao, width=10, command=lambda x=botao: adicionar_caractere(x)).grid(row=row, column=col, columnspan=2, sticky="nsew")
        col += 1
    else:
        tk.Button(janela, text=botao, width=5, command=lambda x=botao: adicionar_caractere(x)).grid(row=row, column=col, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# Botão de limpar
tk.Button(janela, text="C", width=5, command=limpar).grid(row=row, column=col, sticky="nsew")

janela.mainloop()

