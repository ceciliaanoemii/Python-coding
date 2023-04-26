#Lista
lista = ["Cecilia Mogro", "Soy youtuber", True , 1.61]
print(lista)

#Dame el elemento numero 1
print(lista[0]) # el elemento esta en el indice 0

# Las tuplas es igual q una lista con la diferencia que NO se pueden modificar y se usan parentesis ()
tupla = ("Leonardo Aguado", "Soy empleado", False , 1.65)
tupla[2] = "Soy ingieniero" #TE VA A TIRAR ERROR!!
print(tupla) #TE VA A TIRAR ERROR!! LOS DATOS NUNCA SE VAN A MODIFICAR

#Creando un conjunto (set)'. No se puede acceder por indice y no permite repetir valores
conjunto ={"Cecilia Mogro", "Soy youtuber", True , 1.61}

#Creando DICCIONARIO (dict). Parecido a Json

diccionario = {
    'nombre' : "Cecilia Mogro",
    'canal' : "Soy Youtuber",
    'esta_emocionado' : True,
    'altura' : 1.61,
    'dato_duplicado' : "Cecilia Mogro"
}

print (diccionario ['nombre'])