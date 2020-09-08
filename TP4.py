#Nombre del producto------------------------------
N = input("Ingrese el nombre del producto: ")

#Ingreso de Primer Material-----------------------
Materiales={}
M=input("Ingrese el primer material: ")
C=int(input("Ingrese la cantidad que uso: "))
Materiales[M]=C

#Funcion de Menu----------------------------------
def Menu():
	print("Menu de OPCIONES")
	print("1-Agregar Producto")
	print("2-Mostrar el nombre del producto y sus materiales")	
	print("3-Terminar Programa")

#Bucle del Menu-----------------------------------
def ElegirOpcion():
	Estado = 2
	while True:

		Menu()

		Estado=int(input("Ingrese una opcion: "))

		if Estado == 1:
			M=input("Ingrese el material: ")
			C=int(input("Ingrese la cantidad que uso: "))
			Materiales[M]=C

		elif Estado == 2:


		elif Estado == 3:
			print("El Programa se CERRO")
			break

		else:
			print("Introduce una opcion correcta.")


ElegirOpcion()