


n = input("Longitud de la lista: ")

nueva_lista = [ int(input("Ingresa un valor: ")) for _ in range(int(n)) ]

[print(val) for val in nueva_lista if val % 2 == 0 ]