def leerInt(cadena):
    while True:
        try:
            n=int(cadena)
            return n
        except ValueError:
            cadena = input("Error, ingrese un número entero:")