# Excluyendo vocales

# Define una función que nos permita conocer la cantidad de letras, excluyendo vocales, que pose un string.

# El programa deberá cumplir con los siguientes requerimientos.

# La función debe tener por nombre excludes_vowel_counter.
# La función debe recibir como argumento un string.
# La función debe retornar, mediante un número entero, la cantidad de letras, excluyendo vocales que posee el string ingresado.
# Si el string ingresado posee espacios, estos no deberán ser contabilizados


def excludes_vowel_counter(string):
    x = 0

    for c in string.lower():
        if c not in ("","a","e","i","o","u"):
            x +=1
    return x       


excludes_vowel_counter('hola mundo')