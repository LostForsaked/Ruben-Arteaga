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


productos=["Agua mineral", "Manzanas", "Limones"]
precios=[500, 900, 850]
carrito=[]
while True:
    print("1.- Ingresar productos")
    print("2.- Comprar")
    print("3.- Crear Boleta")
    print("4.- Salir")
    op=int(input("Seleccione una opción:\n"))
    match op:
        case 1:
            prod=input("Ingrese el nombre del producto:\n")
            productos.append(prod)
            valor=int(input("Ingrese el precio del producto:\n"))
            precios.append(valor)
            print("Producto ingresado correctamente")
        case 2:
            for i in range(len(productos)):
                print(f"{i+1}.- {productos[i]} - ${precios[i]}")
            print("Seleccione un producto")
            comp=int(input())
            comp=comp-1
            carrito.append(comp)
            print("Producto agregado a su carrito")
        case 3:
            total=0
            print("****************")
            print("*****Boleta*****")
            print("****************")
            for i in carrito:
                print(f"{carrito[i]} ------- {precios[i]}")
                total=total+precios[i]
            print(f"El total de articulos que lleva es {len(carrito)}")
            print(f"el total de su compra es de {total}")
            print(f"el total mas IVA es de {total*1.19}")