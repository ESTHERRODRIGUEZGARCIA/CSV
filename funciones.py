import csv

def funcion1(calificaciones):

    with open("calificaciones.csv", newline='') as file:
        reader = csv.reader(file, delimiter=';')
        calificaciones = []
        n = 0

        for row in reader:
            n+=1
            if n == 1:
                for i in row:
                    calificaciones.append(i)
            else:
                Dictionary1 = {}
                for i in range(len(row)):
                    Dictionary1[calificaciones[i]] = row[i]
                calificaciones.append(Dictionary1)
    file.close()
    return calificaciones

# devuelva una lista de diccionarios, cada dic contiene la información de los exámenes y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.

# Apellidos;Nombre;Asistencia;Parcial1;Parcial2;Ordinario1;Ordinario2;Practicas;OrdinarioPracticas


# crear una función que reciba una lista de diccionarios y añada a cada diccionario un nuevo par con la nota final del curso. El peso de cada parcial de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%.
def funcion2(calificaciones):
    calificaciones = funcion1(calificaciones)

    for i in calificaciones:
        i["Final"] = (float(i["Parcial1"])*0.3 + float(i["Parcial2"])*0.3 + float(i["Ordinario1"])*0.1 + float(i["Ordinario2"])*0.1 + float(i["Practicas"])*0.4 + float(i["OrdinarioPracticas"])*0.4)
    return calificaciones



