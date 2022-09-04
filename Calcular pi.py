# Calcular PI

# π (pi) es sin duda una de las constantes matemáticas más importantes de todos los tiempos. Todos conocemos el valor de π (pi) 
# , bueno, quizás solo sus primeros decimales.

# 3.1415

# Es por ello que en esta ocasión es necesarios que implementes el Problema de Basilea para encontrar el "valor" de π (pi).

# Es obligatorio obtener por lo menos los primeros 6 decimales.

# Pista: Tendrás que multiplicar por 6 y realizar una raíz cuadrada.


import math

suma = 0
for valor in range(1, 100000000):
    suma = suma + (1 / valor ** 2)

pi = math.sqrt(suma * 6)

print(f'El valor de pi es : {pi}')