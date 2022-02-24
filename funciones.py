def menu():
	menu=("Menu:\n1.Ver nombre y correo de cada centro\n2.Contar los centros cuya información se actualizó en un año especificado\n3.Mostrar el fax del centro a partir de su nombre\n4.Ver nombre y nº teléfono de los centros cuyo nº empiece por el dato introducido\n5.Ver nombre,correo y dirección a partir del nº de teléfono\n6. Salir")
	return(menu)

def ejercicio1(datos):
	nombre=[]
	correo=[]
	salida=[]
	for var in 	datos.get("array").get("directorios").get("directorio"):
		nombre.append(var.get("nombre").get("content"))
		correo.append(var.get("correo-electronico"))
	for var in zip(nombre,correo):
		salida.append(var)
	return salida

def ejercicio2(datos):
	lista=[]
	año=input("Introduce el año: ")
	for var in datos.get("array").get("directorios").get("directorio"):
		if año in var.get("send"):
			nombre2=var.get("nombre")
			content=nombre2.get("content")
			lista.append(content)
	return lista

def ejercicio3(datos):
	fax=""
	nombre=input("Introduce el nombre del centro:")
	for var in datos.get("array").get("directorios").get("directorio"):
		if nombre==var.get("nombre").get("content"):
			fax=var.get("fax")
	return fax

def ejercicio4(datos):
	nombre=[]
	telefono=[]
	salida=[]
	dato=input("Introduce un número: ")
	for var in datos.get("array").get("directorios").get("directorio"):
		if dato in var.get("telefono").get("content"):
			nombre.append(var.get("nombre").get("content"))
			telefono.append(var.get("telefono").get("content"))
	for var in zip(nombre,telefono):
		salida.append(var)
	return salida

def ejercicio5(datos):
	dato=input("Introduce un número de teléfono: ")
	dato2=' '.join((dato[:3], dato[3:6], dato[6:9]))
	nombre=[]
	correo=[]
	direccion=[]
	salida=[]
	for var in datos.get("array").get("directorios").get("directorio"):
		telef=var.get("telefono").get("content")
		if dato2==telef[:12] or dato2==telef[13:]:
			nombre.append(var.get("nombre").get("content"))
			correo.append(var.get("correo-electronico"))
			dircc=var.get("direccion")
			dircc2=dircc[1]
			direccion.append(dircc2.get("content"))
	for var in zip(nombre,correo,direccion):
		salida.append(var)
	return salida
