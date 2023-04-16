import tkinter as tk
from tkinter import ttk
import requests

def convertir_moneda(origen, destino, cantidad):
    API_URL = "https://api.exchangerate-api.com/v4/latest/"
    response = requests.get(API_URL + origen)
    tasas = response.json()["rates"]
    tasa_destino = tasas[destino]
    resultado = cantidad * tasa_destino
    return resultado

def convertir():
    moneda_origen = origen_combo.get()
    moneda_destino = destino_combo.get()
    cantidad = float(cantidad_entry.get())
    resultado = convertir_moneda(moneda_origen, moneda_destino, cantidad)
    resultado_label.config(text=f"{cantidad} {moneda_origen} es equivalente a {resultado} {moneda_destino}")

root = tk.Tk()
root.title("Conversor de monedas v2")

origen_label = tk.Label(root, text="Moneda de origen:")
origen_label.grid(row=0, column=0)
monedas = ["USD", "EUR", "JPY", "GBP", "CAD", "CHF", "AUD", "CNY", "HKD", "NZD", "SEK", "KRW", "SGD", "NOK", "MXN", "INR", "RUB", "ZAR", "TRY", "BRL", "TWD", "DKK", "PLN", "THB", "IDR", "HUF", "CZK", "ILS", "CLP", "PHP"]
origen_combo = ttk.Combobox(root, values=monedas)
origen_combo.grid(row=0, column=1)

destino_label = tk.Label(root, text="Moneda de destino:")
destino_label.grid(row=1, column=0)
destino_combo = ttk.Combobox(root, values=monedas)
destino_combo.grid(row=1, column=1)

cantidad_label = tk.Label(root, text="Cantidad:")
cantidad_label.grid(row=2, column=0)
cantidad_entry = tk.Entry(root)
cantidad_entry.grid(row=2, column=1)

convertir_button = tk.Button(root, text="Convertir", command=convertir)
convertir_button.grid(row=3, column=0)

resultado_label = tk.Label(root, text="")
resultado_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
