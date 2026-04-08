def transformar_varias_veces(texto, lista_numeros):
    resultado = texto

    for numero in lista_numeros:
        if numero == 1:
            resultado = resultado.upper()
        elif numero == 2:
            resultado = resultado.lower()
        elif numero == 3:
            resultado = resultado.capitalize()
        else:
            return "Opción inválida"

    return resultado


# Pedir datos al usuario
texto = input("Escribe un texto: ")
entrada = input("Escribe números entre 1 y 3 separados por espacio: ")
lista_numeros = [int(x) for x in entrada.split()]

# Mostrar resultado
print(transformar_varias_veces(texto, lista_numeros))