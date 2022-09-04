def Convert_Decimal_Binary(numero):
    binario = []
    while(numero >=1):
        if numero%2==0:
            binario.append(0)
            numero//=2
        elif numero%2!=0:
            numero//=2
            binario.append(1)
    return(binario[::-1])

def run():
    numero = int(input("Ingrese un numero: "))
    binario = Convert_Decimal_Binary(numero)
    print(f"{binario} es el numero en Binario de {numero}")

run()