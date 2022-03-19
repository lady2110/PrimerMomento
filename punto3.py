#variable controladora
import math
productos =[
	{}
]

print("SuperMercado la Sur")
print("*******")

print("1. Digita 1 Registro de un producto")
print("2. Digita 2 para mostrar todos los productos registrados")
print("3. Digita 3 para buscar por codigo de un producto y editar su precio")
print("4. Digita 4 para buscar por codigo de un producto y eliminar su precio")
print("5. Digita 0 para salir")

print("*******")


opcion=1
while(opcion != 0):
	opcion=int(input("Escoge tu opcion "))
	if(opcion == 5):
		print("Adios")
		break
	elif(opcion == 1):
		codigo = int(input("Ingrese codigo del producto: "))
		nombreproducto= input("Ingrese el nombre del producto: ")
		precio = float(input("Ingrese precio del producto: "))
		producto=dict(codigo=codigo,nombreproducto=nombreproducto,precio=precio)
		productos.append(producto)
	elif(opcion == 2):
		print(productos)
	elif(opcion==3):	
		codigo=int(input("Codigo a buscar: "))
		for producto in productos:
			if(codigo==producto.get('codigo')):
				valoractualizado=float(input("Valor nuevo: "))
				producto.update(precio=valoractualizado)
				print(producto) 
	elif(opcion==4):
		codigo=int(input("Codigo a buscar: "))
		for producto in productos:
			if(codigo==producto.get('codigo')):
				productos.pop(codigo)
				print("producto eliminado")
print(productos) 





	