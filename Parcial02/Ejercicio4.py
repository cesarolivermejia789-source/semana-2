# Paso 1: palabra original
texto = "CANTANDO"

# Paso 2: convertir a minúsculas
texto = texto.lower()

# Paso 3: quitar el sufijo "ando"
texto = texto.replace("ando", "")

# Paso 4: encontrar la posición de la letra "t"
posicion = texto.find("t")

# Mostrar resultados
print(texto)
print(posicion)