import csv

# csv # Apellidos;Nombre;Asistencia;Parcial1;Parcial2;Ordinario1;Ordinario2;Practicas;OrdinarioPracticas;Final
# crear una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.

def funcion1():
    with open("calificaciones.csv", newline='') as file:
        reader = csv.reader(file, delimiter=';')
        calificaciones = []
        n = 0
        lista = []
        for row in reader:
            n+=1
            if n == 1:
                for i in row:
                    lista.append(i)
            else:
                Dictionary1 = {}
                for i in range(len(row)):
                    Dictionary1[lista[i]] = row[i]
                lista.append(Dictionary1)
    file.close()
    return calificaciones



# crear una función que reciba una lista de diccionarios y añada a cada diccionario un nuevo par con la nota final del curso. cada parcial 30%; examen de prácticas 40%.
def funcion2(calificaciones):
    nombre_archivo = "calificaciones.csv"
    # omitir el encabezado
    next(file, None)
    linea = linea.rstrip('\n')
    separador = ";"
    lista = linea.split(separador)
    
    with open(nombre_archivo, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for i in calificaciones:
            i["Final"] = (float(i["Parcial1"]) * 0.3) + (float(i["Parcial2"]) * 0.3) + (float(i["Ordinario1"]) * 0.3) + (float(i["Ordinario2"]) * 0.3) + (float(i["Practicas"]) * 0.4)
            writer.writerow([i["Apellidos"], i["Nombre"], i["Asistencia"], i["Parcial1"], i["Parcial2"], i["Ordinario1"], i["Ordinario2"], i["Practicas"], i["OrdinarioPracticas"], i["Final"]])
    calificaciones = []

    for i in calificaciones:
        i["Final"] = (float(i["Parcial1"])*0.3 + float(i["Parcial2"])*0.3 + float(i["Ordinario1"])*0.1 + float(i["Ordinario2"])*0.1 + float(i["Practicas"])*0.4 + float(i["OrdinarioPracticas"])*0.4)
    return calificaciones

# crear una función que reciba una lista de diccionarios y devuelva dos listas, una con los aprobados y otra con los suspensos. Para aprobar: asistencia mayor o igual que el 75%, nota parciales y prácticas mayor o igual que 4 y nota final mayor o igual que 5.
def funcion3(calificaciones):
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


