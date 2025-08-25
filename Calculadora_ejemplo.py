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

# Crear ventana
ventana = tk.Tk()
ventana.configure(bg="#e0ccd1")  # Color de fondo
ventana.title("Mi calculadora")
ventana.geometry("300x200")  # Tamaño de la ventana

# Entradas
entry1 = tk.Entry(ventana)
entry1.pack(pady=5)

entry2 = tk.Entry(ventana)
entry2.pack(pady=5)

# Botones
tk.Button(ventana, bg="lightpink", text="Sumar", command=lambda: calcular("+")).pack(pady=5)
tk.Button(ventana, bg="lightpink",text="Restar", command=lambda: calcular("-")).pack(pady=5)
tk.Button(ventana, bg="lightpink", text="Multiplicar", command=lambda: mult_div("*")).pack(pady=5)
tk.Button(ventana, bg="lightpink", text="Dividir", command=lambda: mult_div("/")).pack(pady=5)

# Resultado
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado).pack(pady=5)

ventana.mainloop()