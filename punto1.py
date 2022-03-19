contarnumero1=0
contarnumero2=0
contarnumero3=0
numeros=[]
cantidad=int(input("ingrese cantidad de numeros"))

for numero in range(cantidad):
	numero= int(input("Ingrese numero: "))
	numeros.append(numero)
	if(numero % 2 ==0):
		contarnumero1 +=1
	if(numero % 3==0):
		contarnumero2 +=1
	if(numero % 2 == 0 and numero % 3== 0):
		contarnumero3 +=1


print(f"El total de multiplos de 2 : {contarnumero1}")
print(f"El total de multiplos de 3 : {contarnumero2}")
print(f"El total de multiplos de 2 y 3 : {contarnumero3}")


