# print("""
# Carlos leyó un estudio en una revista de salud, la cual recomienda que se debe dormir al menos A horas al día.
#  Quedarse dormido no es saludable, tanto que no debería dormir más de B horas. Carlos ahora duerme H horas por día.
#   Comprueba si Carlos cumple los requerimientos del estudio de la revista.

# Tres variables A, B, H a la entrada en consola.
# A siempre es menor o igual que B.
# Si Carlos duerme menos que A horas debe imprimir Deficiente, si el duerme más de B horas, imprima Exceso.
# Si H se encuentra entre A y B, imprima Normal.
# """)



a = int(input("A: "))
b = int(input("B: "))
h = int(input("H: "))

if h<a:
    print("Deficiente")
elif h>b:
    print("Exceso")
elif a <= h <= b:
    print("Normal")


