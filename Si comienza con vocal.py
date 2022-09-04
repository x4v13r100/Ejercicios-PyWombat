# Comienza con una vocal?

# Desarrolla un programa que nos permita conocer si un string comienza con una vocal.

# El programa debe cumplir con los siguiente requerimientos.

# El usuario podrá ingresar, vía teclado, el String que el usuario desea validar.
# El programa imprimirá en consola, verdadero o falso dependiendo si el ingresado por el usuario comienza o no con una vocal.
import time 
while True:
    vocal= input("Ingrese un String: ")

    vocal= vocal.lower()

    inicia_con = vocal[0] in ["a","e","i","o","u"]

    print(f"Inicia con una vocal: {inicia_con}")

    time.sleep(2)
