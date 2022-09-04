

año=int(input("Ingrese el año que desee: \n"))

def año_bisiesto(año):
    if año%4==0 and año&100!=0:
        return (" El año " + str (año) + " es un año bisiesto.")
    elif año%100==0 and año&400==0:
        return
    else:
        return (f" El año {str(año)} No es bisiesto")

print(año_bisiesto(año))