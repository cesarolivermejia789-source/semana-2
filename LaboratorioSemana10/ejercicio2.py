def transformar(palabra, numero):

    if numero == 1:
        print(palabra.upper())

    elif numero == 2:
        print(palabra.lower())

    elif numero == 3:
        print(palabra.capitalize())

    else:
        print("Número no válido")


# Pedir datos
palabra = input("Escribe una palabra: ")
numero = int(input("Escribe un número (1, 2 o 3): "))

# Llamar a la función
transformar(palabra, numero)