#     -5-4-3 -2 -1
numeros=[7,5,33,24,9]
#      0 1 2  3  4

# print(numeros[-1])

# for numero in numeros:
#     print("numero", numero)


# print(numeros)

# numeros.append(64)

# print(numeros)

# numeros.insert(3,100)

# print(numeros)

# frutas=["Manzana", "Mango", "Membrillo"]

# for fruta in frutas:
#     print(fruta)
# nombres=["shinji", "misato", "asuka"]
# apellidos=["ikari", "katsuragi", "langley"]

# while True:
#     print("1.- Insertar nombre y apellido")
#     print("2.- Mostrar nombres y apellidos")
#     print("3.- Buscar nombre")
#     print("4.- Salir")
#     op=int(input("seleccione una opción \n"))
#     match op:
#         case 1:
#             nom=input("Ingrese un nombre \n")
#             nombres.append(nom)
#             ape=input("Ingrese un apellido")
#             apellidos.append(ape)
#         case 2:
#             # cont=0
#             # for nombre in nombres:
#             #     print(nombres[cont], apellidos[cont])
#             #     cont=cont+1
#             # cont=0
#             for i in range(len(nombres)):
#                 print(nombres[i],apellidos[i])
#         case 3:
#             name=input("ingrese un nombre \n")
#             if name in nombres:
#                 print(f"El nombre {name} existe")
#             else:
#                 print(f"El nombre {name} no existe")
#         case 4:
#             print("Saliendo...")
#             break
#         case _:
#             print("Opción inválida")


# productos=["Agua mineral", "Manzanas", "Limones"]
# precios=[500, 900, 850]
# carrito=[]
# while True:
#     print("1.- Ingresar productos")
#     print("2.- Comprar")
#     print("3.- Crear Boleta")
#     print("4.- Salir")
#     op=int(input("Seleccione una opción:\n"))
#     match op:
#         case 1:
#             prod=input("Ingrese el nombre del producto:\n")
#             productos.append(prod)
#             valor=int(input("Ingrese el precio del producto:\n"))
#             precios.append(valor)
#             print("Producto ingresado correctamente")
#         case 2:
#             for i in range(len(productos)):
#                 print(f"{i+1}.- {productos[i]} - ${precios[i]}")
#             print("Seleccione un producto")
#             comp=int(input())
#             comp=comp-1
#             carrito.append(comp)
#             print("Producto agregado a su carrito")
#         case 3:
#             total=0
#             print("****************")
#             print("*****Boleta*****")
#             print("****************")
#             for i in carrito:
#                 print(f"{carrito[i]} ------- {precios[i]}")
#                 total=total+precios[i]
#             print(f"El total de articulos que lleva es {len(carrito)}")
#             print(f"el total de su compra es de {total}")
#             print(f"el total mas IVA es de {total*1.19}")


import os
import time
notas=[7.0,6.0,4.5]
while True:
    print("1.- Ingresar Nota")
    print("2.- Borrar nota")
    print("3.- Mostrar notas")
    print("4.- Sacar promedio")
    print("5.- Limpiar todas las notas")
    print("6.- Salir")
    op=int(input("Seleccione una opción: \n"))
    os.system("cls")
    time.sleep(1)
    match op:
        case 1:
            print("Ingresar nota")
            cant=int(input("¿Cuántas notas desea ingresar? \n"))
            for i in range(cant):
                grade=float(input("Ingrese una nota en formato decimal: \n"))
                notas.append(grade)
                print("Nota agregada correctamente")
            os.system("cls")
            time.sleep(1)
        case 2:
            print("Borrar nota")
            for i in range(len(notas)):
                print(f"{i+1}.- {notas[i]}")
            n=int(input("Seleccione la nota a borrar; \n"))
            n=n-1
            notas.pop(n)
            os.system("cls")
            time.sleep(1)
        case 3:
            print("Mostrar notas")
            if len(notas)==0:
                print("No hay notas para mostrar")
            else:
                for i in range(len(notas)):
                    print(f"{i+1}.- {notas[i]}")
            time.sleep(3)
            os.system("cls")
        case 4:
            total=0
            print("Sacar promedio, nota mayor y nota menor")
            for i in range(len(notas)):
                total=total+notas[i]
            prom=total/len(notas)
            print(f"El promedio de las notas es: {round(prom,1)}")
            notas.sort()
            print(f"La nota mayor fue {notas[-1]}")
            print(f"La nota menor fue {notas[0]}")
            time.sleep(3)
            os.system("cls")
        case 5:
            print("Limpiar notas")
            notas.clear()
            print("Notas eliminadas")
            time.sleep(1)
            os.system("cls")
        case 6:
            print("Saliendo...")
            break
        case _:
            print("Seleccione una opción válida.")    
vero=[
    [3,4],
    [8,9,64,8]
]
print(vero[1][3])