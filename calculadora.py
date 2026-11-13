import tkinter as tk
from tkinter import messagebox
import re

class Calculadora:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora - Semana 13")
        self.ventana.geometry("400x400")
        self.ventana.resizable(False, False)

        # Display
        self.display = tk.Entry(
            self.ventana,
            font=("Arial", 24),
            justify="right",
            bd=5
        )
        self.display.grid(
            row=0, column=0, columnspan=4,
            sticky="nsew", padx=5, pady=5
        )
#Paso 3: Agregar los botones
        # Definir botones en una matriz
        botones = [
            ('7', '8', '9', '/', None),
            ('4', '5', '6', '*', None),
            ('1', '2', '3', '-', None),
            ('C', '0', '%', '=', '+'),
        ]

        for i, fila in enumerate(botones):
            for j, texto in enumerate(fila):
                if texto is None:
                    continue
                btn = tk.Button(
                    self.ventana,
                    text=texto,
                    font=("Arial", 18),
                    width=4,
                    height=2,
                    command=lambda t=texto: self.click(t)
                )
                if texto == 'C':
                    btn.configure(bg="#F4A6A6", activebackground="#EFA0A0")
                elif texto == '=':
                    btn.configure(bg="#A8D5BA", activebackground="#98C9AA")
                btn.grid(row=i+1, column=j, padx=2, pady=2)
#Paso 4: Implementar la lógica de eventos
    def click(self, valor):
        if valor == 'C':
            self.display.delete(0, tk.END)
        elif valor == '%':
            expresion = self.display.get()
            if re.search(r'(\d+(?:\.\d*)?|\.\d+)$', expresion):
                self.display.insert(tk.END, '%')
            else:
                messagebox.showerror(
                    "Error", "Ingrese un número antes del porcentaje"
                )
        elif valor == '=':
            try:
                expresion = self.resolver_porcentajes(self.display.get())
                resultado = eval(expresion)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(resultado))
            except Exception:
                messagebox.showerror("Error", "Expresión inválida")
                self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, valor)

    def resolver_porcentajes(self, expresion):
        while '%' in expresion:
            coincidencia = re.search(
                r'(\d+(?:\.\d*)?|\.\d+)%', expresion
            )
            if not coincidencia:
                raise ValueError("Expresión de porcentaje inválida")

            valor = float(coincidencia.group(1))
            prefijo = expresion[:coincidencia.start()]
            if prefijo.endswith(('-', '+')) and (
                len(prefijo) == 1 or prefijo[-2] in '+-*/'
            ):
                if prefijo[-1] == '-':
                    valor = -valor
                prefijo = prefijo[:-1]

            operador = re.search(r'([+\-*/])$', prefijo)
            if operador:
                operador_texto = operador.group(1)
                izquierda = prefijo[:operador.start()]
                if operador_texto in '+-' and izquierda:
                    valor = eval(izquierda) * valor / 100
                else:
                    valor /= 100
                prefijo = f"{izquierda}{operador_texto}"
            else:
                valor /= 100

            expresion = (
                f"{prefijo}{valor}{expresion[coincidencia.end():]}"
            )

        return expresion

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    Calculadora().run()