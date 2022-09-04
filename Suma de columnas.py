# Suma de columnas
# Dada una matriz de 3 x 3.

# matriz = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 100],
# ]
# Desarrolla un script el cumpla con los siguientes requerimientos.

# Mostrar en consola la suma de cada una de las columnas de la matriz.
# Mostrar en consola la suma de cada una de las filas de la matriz.
# Mostrar en consola la suma de todas las esquinas de la matriz.
# Los resultados deben estar separados mediante un guión (-)
# Ejemplo.

# La suma de las columnas es: 120 - 150 - 190
# La suma de las filas es: 60 - 250 - 250
# La suma de las esquinas es: 210

# Recuerda que la matriz es de 3 x 3 y no es mutable
# Puedes definir la matiz directamente en tu script.

import time
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 100],
]

columna1 = matriz[0][0] + matriz[1][0] + matriz[2][0]
columna2 = matriz[0][1] + matriz[1][1] + matriz[2][1]
columna3 = matriz[0][2] + matriz[1][2] + matriz[2][2]

fila1 = matriz[0][0] + matriz[0][1] + matriz[0][2]
fila2 = matriz[1][0] + matriz[1][1] + matriz[1][2]
fila3 = matriz[2][0] + matriz[2][1] + matriz[2][2]

corners = matriz[0][0] + matriz[0][2] + matriz[2][0] + matriz[2][2]




print(f"La suma de las Columnas son: Columna 1: {columna1} Columna 2: {columna2} Columna 3: {columna3} ")
print(f"La suma de las Filas son: Fila 1: {fila1} Fila 2: {fila2} Fila 3: {fila3} ")
print(f"La suma de las equina es: {corners}")


time.sleep(1)
print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("...")
time.sleep(1)
print("....")
time.sleep(1)
print(".....")


print("Fin del programa")

