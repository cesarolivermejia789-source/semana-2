# Paso 1: texto original
texto = "Cesar"

# Paso 2: normalización fuerte (ignorar mayúsculas/minúsculas)
texto = texto.casefold()

# Paso 3: verificar si solo tiene letras (True o False)
resultado = texto.isalpha()

# Mostrar resultado
print(texto)
print(resultado)