# Dos listas con [nombre] y [apellido], tenemos que escribir los datos en un archivo de texto
# de forma optima con un FOR

nombres = ["Cecilia","Braian","Pablo","Facundo","Leonardo"]
apellidos = ["Mogro","Coronel","Crudo","Stegman","DiCapo"]

#Registrar esta información en un TXT de forma óptima

with open("archivos_problemas\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-----------\n") for n,a in zip(nombres,apellidos)]
    