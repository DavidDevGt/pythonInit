def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def obtener_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Error: Por favor ingresa un número válido.")

def obtener_operacion():
    while True:
        operacion = input("Elige el tipo de operación (+, -, *, /) o presiona 'q' para salir: ")
        if operacion in ['+', '-', '*', '/']:
            return operacion
        elif operacion == 'q':
            return None
        else:
            print("Operación inválida. Por favor, selecciona una operación válida o presiona 'q' para salir.")

while True:
    num1 = obtener_numero("Ingrese el primer número: ")
    if num1 is None:
        break
    num2 = obtener_numero("Ingrese el segundo número: ")
    if num2 is None:
        break

    operacion = obtener_operacion()
    if operacion is None:
        break

    if operacion == "+":
        resultado = sumar(num1, num2)
    elif operacion == "-":
        resultado = restar(num1, num2)
    elif operacion == "*":
        resultado = multiplicar(num1, num2)
    elif operacion == "/":
        resultado = dividir(num1, num2)

    print("El resultado es:", resultado)
