import tkinter as tk
from tkinter import messagebox
from sympy import Symbol, limit, sympify

def calcular_limite():
    try:
        funcao = entrada_funcao.get()
        ponto = entrada_ponto.get()
        lado = var_lado.get()

        x = Symbol('x')

        funcao_expr = sympify(funcao)
        ponto_valor = sympify(ponto)

        direcao = '+' if lado == "Direita (+)" else '-' if lado == "Esquerda (-)" else ''

        resultado = limit(funcao_expr, x, ponto_valor, dir=direcao)
        messagebox.showinfo("Resultado", f"O limite é: {resultado}")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

janela = tk.Tk()
janela.title("Calculadora de Limites")

tk.Label(janela, text="Função:").grid(row=0, column=0, padx=10, pady=5)
entrada_funcao = tk.Entry(janela, width=30)
entrada_funcao.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Ponto (x →):").grid(row=1, column=0, padx=10, pady=5)
entrada_ponto = tk.Entry(janela, width=30)
entrada_ponto.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Direção:").grid(row=2, column=0, padx=10, pady=5)
var_lado = tk.StringVar(value="Ambos")
opcoes_lado = ["Ambos", "Direita (+)", "Esquerda (-)"]
tk.OptionMenu(janela, var_lado, *opcoes_lado).grid(row=2, column=1, padx=10, pady=5)

botao_calcular = tk.Button(janela, text="Calcular", command=calcular_limite)
botao_calcular.grid(row=3, column=0, columnspan=2, pady=10)

janela.mainloop()
