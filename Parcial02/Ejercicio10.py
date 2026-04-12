# 1. Cadena original
texto = "Python2026"

# 2. Verificar si es alfanumérico (letras y números)
if texto.isalnum():
    print("El texto es alfanumérico")

    # 3. Convertir a minúsculas
    texto_minus = texto.lower()

    # Quitar "2026"
    resultado = texto_minus.replace("2026", "")

    print("Resultado final:", resultado)
else:
    print("El texto NO es alfanumérico")