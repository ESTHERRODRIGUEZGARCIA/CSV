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
                for i in range(len(row)):
                    notas = calificaciones[i].split(',')
                    notas.append(row[i])
                    calificaciones[i] = ','.join(notas)
    file.close()

    return calificaciones





# devuelva una lista de diccionarios, cada dic contiene la información de los exámenes y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.

# Apellidos;Nombre;Asistencia;Parcial1;Parcial2;Ordinario1;Ordinario2;Practicas;OrdinarioPracticas

