import tkinter as tk
from tkinter import messagebox
from sympy import Symbol, limit, sympify

def aVerdadeira():
    try:
        funcao = entradaFuncao.get()
        ponto = entradaPonto.get()
        lado = varLado.get()

        x = Symbol('x')

        funcaoExpr = sympify(funcao)
        pontoValorForget = sympify(ponto)

        direcao = '+' if lado == "Direita (+)" else '-' if lado == "Esquerda (-)" else ''

        resultado = limit(funcaoExpr, x, pontoValorForget, dir=direcao)
        messagebox.showinfo("Resultado", f"O limite é: {resultado}")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

janela = tk.Tk()
janela.title("Calculadora de Limites")

tk.Label(janela, text="Função:").grid(row=0, column=0, padx=10, pady=5)
entradaFuncao = tk.Entry(janela, width=30)
entradaFuncao.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Ponto (x →):").grid(row=1, column=0, padx=10, pady=5)
entradaPonto = tk.Entry(janela, width=30)
entradaPonto.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Direção:").grid(row=2, column=0, padx=10, pady=5)
varLado = tk.StringVar(value="Ambos")
opcoesLado = ["Ambos", "Direita (+)", "Esquerda (-)"]
tk.OptionMenu(janela, varLado, *opcoesLado).grid(row=2, column=1, padx=10, pady=5)

botaoChamarFuncao = tk.Button(janela, text="Calcular", command=aVerdadeira)
botaoChamarFuncao.grid(row=3, column=0, columnspan=2, pady=10)

janela.mainloop()
