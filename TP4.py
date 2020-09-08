#Nombre del producto------------------------------

N = str(input("Ingrese el nombre del producto: "))
print("")

#Ingreso de Primer Material-----------------------

Materiales={}
M=input("Ingrese el primer material: ")
while True:
	try:
		C=int(input("Ingrese la cantidad que uso: "))
		break
	except ValueError:
		print("Los valores introducidos no son correctos")
Materiales[M]=C

#Funcion de Menu----------------------------------

def Menu():
	print(" ")
	print("######################################################")
	print("#              Menu de OPCIONES                      #")
	print("#  1-Agregar producto                                #")
	print("#  2-Mostrar el nombre del producto y sus materiales #")	
	print("#  3-Terminar Programa                               #")
	print("######################################################")
	print(" ")

#Bucle del Menu-----------------------------------

def ElegirOpcion():
	Estado = 2
	while True:

		Menu()
		while True:
			try:
				Estado=int(input("Ingrese una opcion: "))
				break
			except ValueError:
				print("Los valores introducidos no son correctos")

		if Estado == 1:
			M=input("Ingrese el material: ")
			while True:
				try:
					C=int(input("Ingrese la cantidad que uso: "))
					break
				except ValueError:
					print("Los valores introducidos no son correctos")
			Materiales[M]=C

		elif Estado == 2:
			print("El producto es ", N)
			print("La receta para hacer este producto es: ")
			for A,B in Materiales.items():
				print(A, ' --> ', B)


		elif Estado == 3:
			print("El Programa se CERRO")
			break

		else:
			print("Introduce una opcion correcta.")


ElegirOpcion()