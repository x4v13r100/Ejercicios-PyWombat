
# Llaves dentro de un diccionario

# Define una función la cual nos permita conocer todas las llaves dentro de un diccionario. La función debe cumplir con los siguientes requerimientos.

# La función debe tener por nombre sequences_items.
# La función debe recibir como argumento un diccionario.
# La función deberá imprimir en consola cada una de la llaves dentro del diccionario.

# Ayuda:

# El método items sin duda puede serte de mucha útilidad.




mi_diccionario = {'a': 1, 'b': 2, 'c':3, 'd': 4}

def sequences_items(dict):
        for i in dict.keys():
            print(i)


sequences_items(mi_diccionario)




