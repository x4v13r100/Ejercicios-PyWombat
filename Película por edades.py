# Película por edades

# Película por edades
# A partir de las siguientes especificaciones, crea la lógica para recomendar una película dependiendo de la edad dada por el usuario.

# <table> <thead> <tr> <th>Rango de edad</th> <th>Película</th> </tr> </thead> <tbody> <tr> <td><= 16</td> <td>"Coco"*</td> </tr> <tr>
#  <td>17 −− 25</td> <td>"Avengers: Endgame"</td> </tr> <tr> <td>26 −− 40</td> <td>"Matrix"</td> </tr> <tr> <td>41 −− 60</td>
#  <td>"El libro verde"</td> </tr> <tr> <td>> 60</td> <td>"Un golpe con estilo"</td> </tr> </tbody> </table>

while True:
    edad = int(input("Digite su edad: "))

    if edad <= 16:
        print("Coco la pelicula")
    elif 17 <= edad <= 25:
        print("Avengers: Endgame")
    elif 26 <= edad <= 40:
        print("Matrix")
    elif 41 <= edad <= 60:
        print("El libro verde")
    elif edad > 60:
        print("Un golpe con estilo")