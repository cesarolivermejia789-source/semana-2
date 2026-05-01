seguir = "si"

while seguir == "si":   # while repetir
    print("Seleccione nivel:")
    print("1. Fácil")
    print("2. Medio")
    print("3. Difícil")

    nivel = int(input("Ingrese el nivel: "))

    # select case nivel (en Python usamos if/elif)S
    if nivel == 1:
        correcta = 5
        print("¿Cuánto es 2 + 3?")
    elif nivel == 2:
        correcta = 12
        print("¿Cuánto es 3 * 4?")
    elif nivel == 3:
        correcta = 9
        print("¿Cuánto es 3^2?")
    else:
        print("Nivel no válido")
        continue

    # for preguntas (3 intentos)
    for i in range(3):
        respuesta = int(input(f"Intento {i+1}: "))

        # if respuesta
        if respuesta == correcta:
            print("¡Correcto!")
            break
        else:
            print("Incorrecto")

    seguir = input("¿Desea continuar? (si/no): ")

print("Fin del juego")