for numero in range(1, 51):

    if numero % 3 == 0:
        continue

    if numero == 42:
        print("Brecha de seguridad detectada.")
        break

    print(f"Procesando registro ID: {numero}")