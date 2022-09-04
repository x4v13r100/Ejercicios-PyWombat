# Validar correo electrónico

# Ana necesita validar el correo en el login simple que está implementando para su plataforma.

# Detalles:

# Verifica solamente que este contenga @ y punto.
# En la salida debe mostrar al usuario ¡Es válido! o No es válido!.
while True:
    email= input("Ingrese un correo electronico: ")


    if ("@" in email and "." in email and not (",", "*", ":", ";") in email):
        print("Es valido")
    else:
        print("No Es valido")
