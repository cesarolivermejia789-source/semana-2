from decimal import Decimal

total = Decimal("0")

while True:
    try:
        precio = input("Ingrese el precio del producto (0 para salir): ")

        monto = Decimal(precio)

        if monto == 0:
            break

        total += monto

    except ValueError:
        print("Error: Debe ingresar un número válido.")

    except:
        print("Entrada inválida.")

print(f"Total acumulado: ${total}")