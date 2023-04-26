import pandas as pd

#SLIDES : La posicion de inicio SI se incluye, la posicion de final NO se incluye
# cadena= "0123456789"
# print(cadena[:]) --->corre todo (0123456789)
# print(cadena[2:7]) ---> va a mostrar desde el ind 2 al 6 (23456)


#usando la funcion read_csv para leer el archivo CSV
df= pd.read_csv("Archivos\\datos.csv") # df --> data frames
df2= pd.read_csv("Archivos\\datos.csv")

# df= pd.read_csv("Archivos\\datos.csv", names=["name","lastname","age"]) Agregando un encabezado nuevo

#obteniendo los datos de la columna nombre
nombres = df["nombre"]

#ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values("edad")

#ordeandolo de forma descendente
df_orden_descendente = df.sort_values("edad",ascending=False)

#concatenando los 2 dataframes
df_concatenado = pd.concat([df,df2])

#accediendo a la primeras 2 filas con head()
primeras_filas = df.head(2)

#accediendo a las últimas 2 filas con tail()
ultimas_filas = df.tail(2)

#accediendo a la cantidad de filas y columnas con shape (shape es una propiedad, atributo)
filas_totales,columnas_totales = df.shape #desempaquetamos

#obteniendo data estadística del dataframe:
df_info = df.describe()

#accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a la edad de la fila 2 con iloc (indice)
elemento_especifico_iloc = df.iloc[2,2]

#accediendo a todos los apellidos con loc
apellidos_loc = df.loc[:,"apellido"]

#accediendo a todos los apellidos con iloc
apellidos = df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

#accediendo a la fila 3 con iloc
fila_3 = df.iloc[2,:]

#accediendo a filas con edad mayor que 29 con loc
mayor_que_29 = df.loc[df["edad"]>29,:]

print(mayor_que_29)

