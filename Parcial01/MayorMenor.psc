Algoritmo MayorMenor
    Definir num1, num2 Como Real
    
    Escribir "Ingrese el primer número:"
    Leer num1
    
    Escribir "Ingrese el segundo número:"
    Leer num2
    
    Si num1 > num2 Entonces
        Escribir "Mayor: ", num1
        Escribir "Menor: ", num2
    Sino
        Si num1 < num2 Entonces
            Escribir "Mayor: ", num2
            Escribir "Menor: ", num1
        Sino
            Escribir "Ambos números son iguales: ", num1
        FinSi
    FinSi
    
FinAlgoritmo