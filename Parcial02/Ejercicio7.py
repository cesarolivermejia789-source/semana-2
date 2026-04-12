# Paso 1: texto original
texto = "42"

# Paso 2: rellenar con ceros a la izquierda hasta 5 caracteres
texto = texto.zfill(5)

# Paso 3: verificar si termina en "2"
resultado = texto.endswith("2")

# Mostrar resultados
print(texto)
print(resultado)