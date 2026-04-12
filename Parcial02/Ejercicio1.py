# Paso 1: guardar el texto con espacios
animal = "  elefante  "

# Paso 2: quitar los espacios al inicio y al final
animal = animal.strip()

# Paso 3: contar cuántas veces aparece la letra "e"
cantidad = animal.count("e")

# Mostrar resultados
print(animal)
print(cantidad)