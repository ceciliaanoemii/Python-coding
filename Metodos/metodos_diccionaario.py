diccionario = {
    "nombre" : 'Cecilia',
    "apellido" : 'Mogro',
    "subscriptores" : 1000000
}

#nos devuelve un objeto dict_item (tambien nos sirve para iterar)
claves = diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa continùa)

valor_de_kasdks = diccionario.get("kasdks")
print("hola papa, el programa continua")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
#método pop() solo sirve para eliminar UN SOLO elemento. El segundo parametro es para que devuelva 
# un valor predeterminado en caso de no encontrarlo
diccionario.pop("subscriptores")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)