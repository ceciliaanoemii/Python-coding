cadena1 = "Hola,Maquina,Como,Estas"
cadena2 = "Bienvenido maquinola"

# ---- METODOS QUE CONVIERTEN EL VALOR ----
#convierte a mayusculas
mayusc = cadena1.upper()

#convierte a minusculas
minusc = cadena1.lower()

#primera letra en mayuscula... las demas letras la deja en minuscula
primer_letra_mayusc = cadena1.capitalize()

# ---- METODOS QUE BUSCAN UN VALOR ----

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1 . 
# Si hay coincidencia devuelve el indice donde esta esa letra
busqueda_find = cadena1.find("D")

#buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepciòn
busqueda_index = cadena1.index("H")

# ---- METODOS QUE CONSULTAN SI SON NUMERICOS O ALFANUMERICOS ----

#si es numerico, devolvemos true, sino devolvemos false
es_numerico = cadena1.isnumeric()

#si es alfanumèrico devolvemos true (Sin espacios y las letras de la A-Z)
# sino devolvemos false
es_alfanumerico = cadena1.isalpha()

# ---- CUANTAS VECES HAY ----
#contamos coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("la ma")

#contamos cuantos caracteres tiene una cadena. len es una funcion
contar_caracteres = len(cadena1)

# ---- VERIFICACION ----

#verificamos si una cadena empieza con otra cadena dada, si es asì devuelve True
empieza_con = cadena1.startswith("H")

#verificamos si una cadena termina con otra cadena dada, si es asì devuelve True
termina_con = cadena1.endswith("H")

# ---- REEMPLAZAR UN VALOR (Por coma (,) o espacios (" ") ----

#si el valor 1, se encuentra en la cadena original, remplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace(","," ")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")

print(cadena_separada[0])