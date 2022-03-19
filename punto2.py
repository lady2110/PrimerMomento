frutas=[]
for fruta in range(0,10,1):
	registrofruta=input("Ingresa una fruta: ")
	frutas.append(registrofruta)

print(frutas)

frutasinversas = [fruta for fruta in reversed(frutas)]
print(frutasinversas)