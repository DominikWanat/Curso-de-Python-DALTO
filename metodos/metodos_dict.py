diccionario = {
    "nombre" : "lucas",
    "apellido" : "dalto",
    "subs" : 1000000
}

#devuelve las claves del diccionaro
claves = diccionario.keys()

#nos muestra el valor del elemento con get (si no lo encuentra el programa continua)
valor_de_nombre = diccionario.get("nombre")

#eliminando un elemento del diccionario
diccionario.pop("subs")

#obteniendo un elemento dict_itesms iterable
diccionario_iterable = diccionario.items()


print(diccionario_iterable)

#vaciando el diccionario
#diccionario.clear()