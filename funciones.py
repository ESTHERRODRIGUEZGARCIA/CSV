import csv

# csv # Apellidos;Nombre;Asistencia;Parcial1;Parcial2;Ordinario1;Ordinario2;Practicas;OrdinarioPracticas;Final
# crear una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.

def funcion1():
    nombre_archivo = "calificaciones.csv"
    with open(nombre_archivo, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader, None) # omitir el encabezado
        notas = []
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
            notas.append(i)
            print(f"Apellidos: {Apellidos}\nNombre: {Nombre}\n% de Asistencia: {Asistencia}\nParcial 1: {Parcial1}\nParcial 2: {Parcial2}\nOrdinario 1: {Ordinario1}\nOrdinario 2: {Ordinario2}\nPrácticas: {Practicas}\nOrdinario Prácticas: {OrdinarioPracticas}\n")
        csvfile.close()

funcion1()


# Apellidos;Nombre;Asistencia;Parcial1;Parcial2;Ordinario1;Ordinario2;Practicas;OrdinarioPracticas;Final
# crear una función que reciba una lista de diccionarios y añada a cada diccionario un nuevo par con la nota final del curso. cada parcial 30%; examen de prácticas 40%.
def funcion2():
    nombre_archivo = "calificaciones.csv"
    with open(nombre_archivo, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        notafinal = 0
        for i in reader:
            Apellidos = i[0]
            Nombre = i[1]
            Parcial1 = i[3]
            Parcial2 = i[4]
            Ordinario1 = i[5]
            Ordinario2 = i[6]
            Practicas = i[7]
            OrdinarioPracticas = i[8]
            notas = [Parcial1, Parcial2, Ordinario1, Ordinario2, Practicas, OrdinarioPracticas]

            for i in range(len(notas)):
                if type(notas[i]) != float:
                    notas[i] = float(notas[i])

            nota_final = (notas[0]*0.3) + (notas[1]*0.3) + (notas[2]*0.3) + (notas[3]*0.3) + (notas[4]*0.4) + (notas[5]*0.4)
            i.append(nota_final)
        print(f"Nombre y Apellidos: '{Nombre} {Apellidos} con una nota final de {notafinal}")
        file.close()
# float(i["Parcial1"])
funcion2()



# crear una función que reciba una lista de diccionarios y devuelva dos listas, una con los aprobados y otra con los suspensos. Para aprobar: asistencia mayor o igual que el 75%, nota parciales y prácticas mayor o igual que 4 y nota final mayor o igual que 5.
def funcion3():
    with open("calificaciones.csv", newline='') as file:
        reader = csv.reader(file, delimiter=';')
        aprobados = []
        suspensos = []
        for i in reader:
            Asistencia = i[2]
            Parcial1 = i[3]
            Parcial2 = i[4]
            Ordinario1 = i[5]
            Ordinario2 = i[6]
            Practicas = i[7]
            OrdinarioPracticas = i[8]
            notafinal = float(Parcial1) * 0.3 + float(Parcial2) * 0.3 + float(Ordinario1) * 0.3 + float(Ordinario2) * 0.3 + float(Practicas) * 0.4 + float(OrdinarioPracticas) * 0.4
            if float(Asistencia) >= 75 and float(Parcial1) >= 4 and float(Parcial2) >= 4 and float(Ordinario1) >= 4 and float(Ordinario2) >= 4 and float(Practicas) >= 4 and float(OrdinarioPracticas) >= 4 and float(notafinal) >= 5:
                aprobados.append(i)
            else:
                suspensos.append(i)
        file.close()
        print(f"Los aprobados son: {aprobados}")
        print(f"Los suspensos son: {suspensos}")

funcion3()
