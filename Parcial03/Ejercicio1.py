

etiqueta = input("Ingrese la etiqueta de rastreo: ")

# Validación 
if etiqueta == "" or etiqueta is None:
    print("Error: La etiqueta no puede estar vacía.")
else:
    # usando slicing
    inicio = etiqueta.find("-") + 1
    fin = etiqueta.rfind("-")

    categoria = etiqueta[inicio:fin]

    print("Categoría:", categoria)

    ruta = "Ruta Local" if etiqueta[-2:] == "SV" else "Ruta Internacional"

    print(ruta)