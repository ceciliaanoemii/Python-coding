#creando diccionarios con dict()
diccionario = dict(nombre="cecilia",apellido="mogro")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["mogro","rancio" ]):"jajas"}

#creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre","apellido"])

#creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"],"No se")



print(diccionario["nombre"])
