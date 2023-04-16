import tkinter as tk
import requests

def convertir_moneda(origen, destino, cantidad):
    API_URL = "https://api.exchangerate-api.com/v4/latest/"
    response = requests.get(API_URL + origen)
    tasas = response.json()["rates"]
    tasa_destino = tasas[destino]
    resultado = cantidad * tasa_destino
    return resultado

def convertir():
    moneda_origen = origen_entry.get()
    moneda_destino = destino_entry.get()
    cantidad = float(cantidad_entry.get())
    resultado = convertir_moneda(moneda_origen, moneda_destino, cantidad)
    resultado_label.config(text=f"{cantidad} {moneda_origen} es equivalente a {resultado} {moneda_destino}")

root = tk.Tk()
root.title("Conversor de monedas")

origen_label = tk.Label(root, text="Moneda de origen:")
origen_label.grid(row=0, column=0)
origen_entry = tk.Entry(root)
origen_entry.grid(row=0, column=1)

destino_label = tk.Label(root, text="Moneda de destino:")
destino_label.grid(row=1, column=0)
destino_entry = tk.Entry(root)
destino_entry.grid(row=1, column=1)

cantidad_label = tk.Label(root, text="Cantidad:")
cantidad_label.grid(row=2, column=0)
cantidad_entry = tk.Entry(root)
cantidad_entry.grid(row=2, column=1)

convertir_button = tk.Button(root, text="Convertir", command=convertir)
convertir_button.grid(row=3, column=0)

resultado_label = tk.Label(root, text="")
resultado_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
