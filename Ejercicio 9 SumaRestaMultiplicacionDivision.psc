Algoritmo SumaRestaMultiplicacionDivision
	
	Definir entero1, entero2,entero3, total Como Entero
	
	Escribir "Digite el primer numero"
	leer entero1
	
	Escribir "Digite el segundo numero"
	leer entero2
	

	
	total = entero1 + entero2 
	Escribir "La suma de los 2 numeros es:" , total
	
	
	total = entero1 - entero2 
	Escribir "La resta de los 2 numeros es:" , total
	
	
	total = entero1 * entero2 
	Escribir "La multiplicacion de los 2 numeros es:" , total
	
	Si entero2 > 0 Entonces
	total = entero1 / entero2 
	Escribir "La división de los 2 numeros es:" , total
	SiNo
	Escribir "No se puede dividir un numero con 0"
	Finsi
	
FinAlgoritmo