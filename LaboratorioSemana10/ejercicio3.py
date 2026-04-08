def transformar_lista(lista, numero):

    for palabra in lista:

        if numero == 1:
            print(palabra.upper())

        elif numero == 2:
            print(palabra.lower())

        elif numero == 3:
            print(palabra.capitalize())

        else:
            print("Número no válido")
            break


# Pedir datos
lista = input("Escribe palabras separadas por espacio: ").split()
numero = int(input("Escribe un número (1, 2 o 3): "))

# Llamar función
transformar_lista(lista, numero)