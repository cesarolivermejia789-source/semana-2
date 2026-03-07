Algoritmo SumaNumerosPositivos
    Definir numero, suma Como Real
    
    suma <- 0
    
    Repetir
        Escribir "Ingrese un número (negativo para terminar):"
        Leer numero
        
        Si numero >= 0 Entonces
            suma <- suma + numero
        FinSi
        
    Hasta Que numero < 0
    
    Escribir "La suma de los números positivos es: ", suma
    
FinAlgoritmo
