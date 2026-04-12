# 1. Nombre de archivo
archivo = "Cesar.txt"

# 2. Quitar el sufijo ".txt"
limpio = archivo.replace(".txt", "")

# Quitar el prefijo "ING. "
limpio = limpio.replace("ING. ", "")

# 3. Convertir a minúsculas
resultado = limpio.lower()

print(resultado)