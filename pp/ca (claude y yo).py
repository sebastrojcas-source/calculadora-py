import tkinter as tk


# ---------- LÓGICA (es tu mismo if / elif / else) ----------
def calcular(operacion):
    # Leemos los dos números de las cajas de texto
    try:
        numero1 = float(entrada1.get())
        numero2 = float(entrada2.get())
    except ValueError:
        resultado.config(text='Escribe dos números válidos')
        return

    if operacion == '+':
        texto = 'el resultado de la suma es: ' + str(numero1 + numero2)
    elif operacion == '-':
        texto = 'el resultado de la resta es: ' + str(numero1 - numero2)
    elif operacion == '*':
        texto = 'el resultado de la multiplicacion es: ' + str(numero1 * numero2)
    elif operacion == '/':
        if numero2 == 0:
            texto = 'no se puede dividir por cero'
        else:
            texto = 'el resultado de la division es: ' + str(numero1 / numero2)
    elif operacion == '%':
        if numero2 == 0:
            texto = 'no se puede dividir por cero'
        else:
            texto = 'el residuo de la division es: ' + str(numero1 % numero2)
    else:
        texto = 'operacion no valida'

    resultado.config(text=texto)


def limpiar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    resultado.config(text='')
    entrada1.focus()


# ---------- VENTANA ----------
ventana = tk.Tk()
ventana.title('Calculadora')
ventana.geometry('380x330')
ventana.resizable(False, False)

# Bienvenida (tus print del inicio)
tk.Label(ventana, text='Hola bienvenido a calculadora',
         font=('Arial', 14, 'bold')).pack(pady=10)

# Datos del usuario
tk.Label(ventana, text='Digita tu primer numero').pack()
entrada1 = tk.Entry(ventana, font=('Arial', 12), justify='center')
entrada1.pack(pady=3)

tk.Label(ventana, text='Digita tu segundo numero').pack()
entrada2 = tk.Entry(ventana, font=('Arial', 12), justify='center')
entrada2.pack(pady=3)

# Botones de operaciones (reemplazan el input de 'elige tu ecuacion')
tk.Label(ventana, text='Elige tu ecuacion').pack(pady=5)
marco_botones = tk.Frame(ventana)
marco_botones.pack()

for simbolo in ['+', '-', '*', '/', '%']:
    tk.Button(marco_botones, text=simbolo, width=4, font=('Arial', 12),
              command=lambda s=simbolo: calcular(s)).pack(side='left', padx=3)

tk.Button(ventana, text='Limpiar', command=limpiar).pack(pady=10)

# Aquí aparece el resultado
resultado = tk.Label(ventana, text='', font=('Arial', 11, 'bold'),
                     wraplength=340, fg='darkgreen')
resultado.pack(pady=5)

ventana.mainloop()