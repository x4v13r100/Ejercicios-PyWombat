
# Elimina elementos duplicados de una lista.

# Dada una lista de números enteros.


# Desarrolla una función que elimine todos los elementos duplicados dentro de la colección.

# La función debe cumplir con los siguientes requerimientos.

# La función debe tener por nombre simple\list.
# La función debe recibir como argumento una lista de números enteros.
# La función debe retornar una lista con elementos únicos dentro de ella.
# Si dentro de la lista existen 2 o más elementos duplicados, la lista debe retornar únicamente un elemento unico.
# Ejemplo.




lista_a = [1, 2, 3, 2, 10, 20, 10, 2, 3, 4, 5, 2, 2] 


# lista_b = [110, 20, 45, 50] 


# lista_c = [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4] 



def simple_list(numeros):
    duplicados = list()
    simples = list()

    for i in numeros:
        if i not in duplicados:
            simples.append(i)
            duplicados.append(i)

    return simples


simple_list(lista_a)

x = simple_list(lista_a)

print(x)
