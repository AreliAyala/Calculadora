import tkinter as tk

# Función que hace la operación
def calcular(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if op == "+":
            resultado.set(num1 + num2)
        elif op == "-":
            resultado.set(num1 - num2)
    except ValueError:
        resultado.set("Error")
def mult_div(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if op == "*":
            resultado.set(num1 * num2)
        elif op == "/":
            resultado.set(num1 / num2)
    except ValueError:
        resultado.set("Error")
def factorial(op):
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        if op == "!":
            if num1 == 0 or num1 == 1:
                resultado.set(1)
            else:
                fact1 = 1
                for i in range(2, num1 + 1):
                    fact1 *= i
                fact2 = 1
                for j in range(2, num2 + 1):
                    fact2 *= j
                resultado.set(f"{num1}!= {fact1}.                     {num2}!= {fact2}.")
    except ValueError:
        resultado.set("Error")
# Crear ventana

ventana = tk.Tk()
frame_grid = tk.Frame(ventana)
frame_grid.pack(pady=10)
ventana.configure(bg="#e0ccd1")  # Color de fondo
ventana.title("Mi calculadora")
ventana.geometry("300x350")  # Tamaño de la ventana

# Entradas
entry1 = tk.Entry(frame_grid)
entry1.grid(row=0, column=0,sticky="e", padx=5, pady=5)

entry2 = tk.Entry(frame_grid)
entry2.grid(row=0, column=1,sticky="e", padx=5, pady=5)

# Botones
frame_pack = tk.Frame(ventana)
frame_pack.pack(pady=10)
tk.Button(ventana, bg="lightpink", text="Sumar", command=lambda: calcular("+")).pack(pady=5)
tk.Button(ventana, bg="lightpink",text="Restar", command=lambda: calcular("-")).pack(pady=5)
tk.Button(ventana, bg="lightpink", text="Dividir", command=lambda: mult_div("/")).pack(pady=5)
tk.Button(ventana, bg="lightpink", text="Multiplicar", command=lambda: mult_div("*")).pack(pady=5)
tk.Button(ventana, bg="lightpink", text="Factorial de ambos números", command=lambda: factorial("!")).pack(pady=5)

# Resultado
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado).pack(pady=20)

ventana.mainloop()