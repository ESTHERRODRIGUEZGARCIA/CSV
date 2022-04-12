import csv

# csv # Apellidos;Nombre;Asistencia;Parcial1;Parcial2;Ordinario1;Ordinario2;Practicas;OrdinarioPracticas;Final
# crear una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.

def funcion1():
    nombre_archivo = "calificaciones.csv"
    with open(nombre_archivo, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader, None) # omitir el encabezado
        calificaciones = []
        for i in reader:
            Apellidos = i[0]
            Nombre = i[1]
            Asistencia = i[2]
            Parcial1 = i[3]
            Parcial2 = i[4]
            Ordinario1 = i[5]
            Ordinario2 = i[6]
            Practicas = i[7]
            OrdinarioPracticas = i[8]
            for i in nombre_archivo:
                print(f"Apellidos: '{Apellidos}, Nombre: {Nombre}, % de Asistencia: {Asistencia}, Parcial 1: {Parcial1}, Parcial 2: {Parcial2}, Ordinario 1: {Ordinario1}, Ordinario 2: {Ordinario2}, Prácticas: {Practicas}, Ordinario Prácticas: {OrdinarioPracticas}\n")
            file.close()
            calificaciones.append(i)
        file.close()
        return calificaciones
funcion1()




# Apellidos;Nombre;Asistencia;Parcial1;Parcial2;Ordinario1;Ordinario2;Practicas;OrdinarioPracticas;Final
# crear una función que reciba una lista de diccionarios y añada a cada diccionario un nuevo par con la nota final del curso. cada parcial 30%; examen de prácticas 40%.
def funcion2():
    nombre_archivo = "calificaciones.csv"
    with open(nombre_archivo, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for i in reader:
            Apellidos = i[0]
            Nombre = i[1]
            Parcial1 = i[3]
            Parcial2 = i[4]
            Ordinario1 = i[5]
            Ordinario2 = i[6]
            Practicas = i[7]
            OrdinarioPracticas = i[8]
            Final = ( {Parcial1} + {Parcial2} + {Ordinario1} + {Ordinario2} )* 0.3 + ( {Practicas} + {OrdinarioPracticas} ) * 0.4
            for i in nombre_archivo:
                print(f"Nombre y Apellidos: '{Nombre} {Apellidos} con una nota final de {Final}")
            file.close()
funcion2()


# crear una función que reciba una lista de diccionarios y devuelva dos listas, una con los aprobados y otra con los suspensos. Para aprobar: asistencia mayor o igual que el 75%, nota parciales y prácticas mayor o igual que 4 y nota final mayor o igual que 5.
def funcion3():
    with open("calificaciones.csv", newline='') as file:
        reader = csv.reader(file, delimiter=';')
        calificaciones = []
        aprobados = []
        suspensos = []
        for i in calificaciones:
            if float(i["Asistencia"]) >= 75 and float(i["Parcial1"]) >= 4 and float(i["Parcial2"]) >= 4 and float(i["Ordinario1"]) >= 4 and float(i["Ordinario2"]) >= 4 and float(i["Practicas"]) >= 4 and float(i["OrdinarioPracticas"]) >= 4 and float(i["Final"]) >= 5:
                aprobados.append(i)
            else:
                suspensos.append(i)
        file.close()
        return aprobados, suspensos

funcion3()
