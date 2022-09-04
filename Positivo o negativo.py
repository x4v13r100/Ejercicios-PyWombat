# Positivo o negativo

# Mario necesita ayuda para identificar si el número es Positivo, Negativo o Cero dado en consola.

while True:
    numero= int(input("Ingrese un numero: "))

    if (numero > 0):
        print("Positivo")
    elif (numero == 0):
        print("Cero")
    else:
        print("Negativo")
