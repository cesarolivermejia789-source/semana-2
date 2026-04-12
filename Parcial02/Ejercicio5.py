# Paso 1: cadena original
texto = "pYTHON"

# Paso 2: cambiar mayúsculas por minúsculas y viceversa
texto = texto.swapcase()

# Paso 3: alinear a la izquierda en 15 espacios y rellenar con "*"
texto = texto.ljust(15, "*")

# Mostrar resultado
print(texto)