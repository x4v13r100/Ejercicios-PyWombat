# Tres ángulos

# A partir de 3 ángulos (A, B, C) dado en la entrada por el usuario, diga si estos conforman un triángulo.

# Pista: La suma de los tres ángulos internos es igual a 180 grados.

# Salida: ¡Es un triángulo! o ¡No es un triángulo! en dependencia del resultado.


while range(3):

    a = int(input("Lado A: "))
    b = int(input("Lado B: "))
    c = int(input("Lado C: "))

    resultado = a+b+c


    if resultado == 180:
        print("Es un Triangulo")
    else:
        print("No es un Triangulo")
    


