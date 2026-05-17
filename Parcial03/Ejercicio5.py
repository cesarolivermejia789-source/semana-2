

nombre_completo = input("Ingrese su nombre completo: ")

lista_nombre = nombre_completo.split()

lista_invertida = lista_nombre[::-1]

print("Nombre transformado:")

for palabra in lista_invertida:

    for letra in palabra:
        print(letra, end=".")

    print("\n")