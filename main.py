from funciones import funcion1, funcion2, funcion3

if __name__ == "__main__":
    calificaciones = funcion1()
    aprobados, suspensos = funcion3(calificaciones)
    print(f"Aprobados: {aprobados}")
    print(f"Suspensos: {suspensos}")
    print(f"Calificaciones: {calificaciones}")

    print("Fin del programa")


