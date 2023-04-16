import tkinter as tk
import random
import string
import pyperclip

def generar_contrasena():
    longitud = int(longitud_entry.get())
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    contrasena_entry.delete(0, tk.END)
    contrasena_entry.insert(0, contrasena)

def copiar_contrasena():
    contrasena = contrasena_entry.get()
    pyperclip.copy(contrasena)

# Crear ventana principal
root = tk.Tk()
root.title("Generador de contraseñas")

# Crear campos de entrada
longitud_label = tk.Label(root, text="Longitud:")
longitud_label.grid(row=0, column=0)
longitud_entry = tk.Entry(root)
longitud_entry.grid(row=0, column=1)

# Crear botón de generación de contraseña
generar_button = tk.Button(root, text="Generar", command=generar_contrasena)
generar_button.grid(row=1, column=0)

# Crear campo de salida para la contraseña generada
contrasena_label = tk.Label(root, text="Contraseña generada:")
contrasena_label.grid(row=2, column=0)
contrasena_entry = tk.Entry(root)
contrasena_entry.grid(row=2, column=1)

# Crear botón de copiar al portapapeles
copiar_button = tk.Button(root, text="Copiar al portapapeles", command=copiar_contrasena)
copiar_button.grid(row=3, column=1)

root.mainloop()
