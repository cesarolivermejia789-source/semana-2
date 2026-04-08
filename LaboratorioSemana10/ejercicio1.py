def funcion(texto, numero):

    if numero == 1:
        return texto.upper()

    if numero == 2:
        return texto.lower()

    if numero == 3:
        return texto.capitalize()


# Pedir datos al usuario
texto = input("Escribe un texto: ")
numero = int(input("Escribe un número (1, 2 o 3): "))

# Mostrar resultado
print(funcion(texto, numero))