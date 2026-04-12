# 1. Cadena original
texto = "  el nido matinal  "

# 2. Quitar espacios y poner mayúscula en cada palabra
texto_limpio = texto.strip()
texto_formateado = texto_limpio.title()

print(texto_formateado)

# 3. Centrar en 30 caracteres con guiones "-"
resultado = texto_formateado.center(30, "-")

print(resultado)