# Contador de vocales dentro de un string

# Define una función que nos permita conocer la cantidad de vocales que posea un string.

# El programa deberá cumplir con los siguientes requerimientos.

# La función debe tener por nombre vowel_counter.
# La función debe recibir como argumento un string.
# La función debe retornar, mediante un número entero, la cantidad de vocales que posee el string ingresado.

def vowel_counter(string):
    x = 0

    for c in string.lower():
        if c in ("a", "e", "i", "o", "u"):
             x+=1
    return x

vowel_counter('hola mundo')



