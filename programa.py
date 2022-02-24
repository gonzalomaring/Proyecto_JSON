import json
from funciones import *
with open("centros.json") as fichero:
    datos=json.load(fichero)
print(menu())
opcion=int(input("Elige una opción: "))
while opcion!=6:
    if opcion==1:
        for a in nombreycorreo(datos):
            print("El nombre es",a[0],"y su correo es",a[1])
        opcion=int(input("Elige una opción: "))
    elif opcion==2:
        año=input("Introduce el año: ")
        for a in contar_actualizacion(datos,año):
            print("El centro",a,"ha tenido una actualización de su información en el año introducido")
        opcion=int(input("Elige una opción: "))
    elif opcion==3:
            nombre=input("Introduce el nombre del centro: ")
            print("El fax es",verfax(datos,nombre))
            opcion=int(input("Elige una opción: "))
    elif opcion==4:
        numero=input("Introduce un número: ")
        for a in telefono_completo(datos,numero):
            print("El nombre es",a[0],"y el número completo es",a[1])
        opcion=int(input("Elige una opción: "))
    elif opcion==5:
        telefono=input("Introduce un número de teléfono: ")
        for a in nombre_correo_direccion(datos,telefono):
            print("El nombre es",a[0],"el correo es",a[1],"y la dirección del centro es",a[2])
        opcion=int(input("Elige una opción: "))
    elif opcion==7:
        print(menu())
        opcion=int(input("Elige una opción: "))
    else:
        print("Opción incorrecta, pulsa 7 para ver el menú")
        opcion=int(input("Elige una opción: "))
print("Adiós!")
