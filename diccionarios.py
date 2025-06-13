# un diccionario es un conjunto de pares de datos

# dic={
#     "nombre":"Mel Brooks",
#     "numero":945453443,
#     "casado": True
# }

# # print(dic)

# for key,value in dic.items():
#     print(key,value)

# dic["ciudad"]="Talca"

# for key,value in dic.items():
#     print(key,value)

# dic["casado"]=False

# for key,value in dic.items():
#     print(key,value)

# frutas={
#     "sandia": 3000,
#     "manzana": 1500,
#     "naranja": 1000
# }

# print(frutas)
# fruta=input("Ingrese una fruta \n")
# precio=int(input("Ingrese el precio de la fruta \n"))

# frutas[fruta]=precio

# print(frutas)

frutas={
    "manzana":1500,
    "frutilla":1000
}
while True:
    print("1.- Ingresar fruta y precio")
    print("2.- Actualizar precio")
    print("3.- Borrar fruta y precio")
    print("4.- Mostrar todas las frutas y precios")
    print("5.- Comprar")
    print("6.- Salir")
    op=int(input("Seleccione una opción: \n"))
    match op:
        case 1:
            print("Ingresar fruta y precio")
            fruit=input("Ingrese el nombre de la fruta:\n")
            valor=int(input("Ingrese el precio de la fruta: \n"))
            frutas[fruit]=valor
            print("Fruta agregada correctamente")
        case 2:
            print("Actualizar precio")
            for key,value in frutas.items():
                print(key,value)
            choice=input("Qué fruta desea actualizar?\n")
            price=int(input("Ingrese el nuevo valor\n"))
            frutas[choice]=price
            print("Fruta actualizada correctamente")
        case 3:
            print("Borrar fruta y precio")
            for key,value in frutas.items():
                print(key,value)
            choice=input("Qué fruta desea borrar?\n")
            del frutas[choice]
            print("Fruta borrada correctamente")
        case 4:
            print("Mostrar todas las frutas y precios\n")
            for key,value in frutas.items():
                print(key,value)
        case 5:
            print("Comprar")
            
        case 6:
            print("Saliendo...")
            break
        case _:
            print("Seleccione una opción válida")



