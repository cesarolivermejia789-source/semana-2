Algoritmo CalificacionEstudiante
    Definir nota Como Real
    
    Escribir "Ingrese la nota del estudiante:"
    Leer nota
    
    Si nota > 10 Entonces
        Escribir "Error: la nota no puede ser mayor que 10"
    Sino
        Si nota >= 6 Entonces
            Escribir "Aprobado"
        Sino
            Si nota <= 4 Entonces
                Escribir "Reprobado"
            Sino
                Escribir "Recuperación"
            FinSi
        FinSi
    FinSi
    
FinAlgoritmo