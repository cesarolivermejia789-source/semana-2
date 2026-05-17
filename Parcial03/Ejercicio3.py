temperaturas = []

# Solicitar temperaturas
for i in range(5):
    dato = int(input(f"Ingrese la temperatura {i + 1}: "))
    temperaturas.append(dato)


for temperatura in temperaturas:

    match temperatura:

        case 0:
            print("Alerta: Punto de Congelación")

        case 100:
            print("Alerta: Punto de Ebullición")

        case _:
            estado = "Estado: Estable" if 10 <= temperatura <= 30 else "Estado: Crítico"
            print(estado)