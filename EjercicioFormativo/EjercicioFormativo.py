# Sistema de registro de estudiantes y notas

nombres = []
notas = []

while True:

    print("\n===== MENU =====")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Mostrar promedio general")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ")

    # match-case para el menú
    match opcion:

        case "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            nota = float(input("Ingrese la nota: "))

            nombres.append(nombre)
            notas.append(nota)

            print("Estudiante agregado correctamente")

        case "2":
            if len(nombres) == 0:
                print("No hay estudiantes registrados")

            else:
                print("\n=== LISTA DE ESTUDIANTES ===")

                # for para recorrer listas
                for i in range(len(nombres)):

                    # if y elif para clasificar
                    if notas[i] >= 9:
                        estado = "Excelente"

                    elif notas[i] >= 7:
                        estado = "Aprobado"

                    elif notas[i] >= 6:
                        estado = "Regular"

                    else:
                        estado = "Reprobado"

                    print("Nombre:", nombres[i])
                    print("Nota:", notas[i])
                    print("Estado:", estado)
                    print("-------------------")

        case "3":
            buscar = input("Ingrese el nombre a buscar: ")
            encontrado = False

            for i in range(len(nombres)):
                if nombres[i].lower() == buscar.lower():

                    print("\nEstudiante encontrado")
                    print("Nombre:", nombres[i])
                    print("Nota:", notas[i])

                    encontrado = True

            if encontrado == False:
                print("Estudiante no encontrado")

        case "4":
            if len(notas) == 0:
                print("No hay notas registradas")

            else:
                suma = 0

                for nota in notas:
                    suma = suma + nota

                promedio = suma / len(notas)

                print("Promedio general:", promedio)

        case "5":
            print("Saliendo del programa...")
            break

        case _:
            print("Opcion no valida")