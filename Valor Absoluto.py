
# Valor absoluto

# Desarrolla una función que nos permite obtener el valor absoluto de un número.

# La función debe cumplir con los siguientes requerimientos.

# La función debe tener por nombre absoluto.
# La función debe recibir de forma obligatoria un número entero.
# La función debe retornar el valor absoluto de dicho número.



def absoluto(numero):
    if numero == 0:
        return 0

    if numero < 0:
        return numero * -1
    else:
        return numero