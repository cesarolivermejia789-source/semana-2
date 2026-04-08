def transformar_lista(lista, numero):

    for palabra in lista:

        if numero == 1:
            print(palabra.upper())

        elif numero == 2:
            print(palabra.lower())

        elif numero == 3:
            print(palabra.capitalize())

        else:
            print("Opción inválida")
            break


# Pedir datos al usuario
texto = input("Escribe varias palabras separadas por espacio: ")
lista = texto.split()
numero = int(input("Escribe un número (1, 2 o 3): "))

# Llamar la función
transformar_lista(lista, numero)