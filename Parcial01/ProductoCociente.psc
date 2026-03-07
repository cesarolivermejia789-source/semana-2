Algoritmo ProductoCociente
    Definir num1, num2, producto, cociente Como Real
    
    Escribir "Ingrese el primer número:"
    Leer num1
    
    Escribir "Ingrese el segundo número:"
    Leer num2
    
    producto <- num1 * num2
    
    Si num2 <> 0 Entonces
        cociente <- num1 / num2
        Escribir "El cociente es: ", cociente
    Sino
        Escribir "Error: no se puede dividir entre 0"
    FinSi
    
    Escribir "El producto es: ", producto
    
FinAlgoritmo
