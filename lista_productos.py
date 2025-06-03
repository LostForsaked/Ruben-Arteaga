lista_productos=[]
cont=0
def agregar():
    global lista_productos
    while True:
        print("Qué producto desea agregar?")
        producto=input()
        lista_productos.append(producto)
        choice=input("para seguir agregando productos, pulse enter. Para salir, pulse X \n")
        if choice=="x" or choice=="X":
            break
def eliminar():
    global lista_productos
    lista_productos.sort()
    for e in lista_productos:
        print(e)
    while True:
        try:
            delete=input("Qué producto desea eliminar? \n")
            lista_productos.remove(delete)
            choice=input("para seguir agregando productos, pulse enter. Para salir, pulse X \n")
            if choice=="x" or choice=="X":
                break
        except Exception:
            print("Error. El producto no se encuentra en la lista")
            break
def mostrar():
    global lista_productos
    lista_productos.sort()
    for e in lista_productos:
        print(e)

while True:
    try:
        op=int(input("Seleccione una opción: \n1.- Agregar productos \n2.- Eliminar productos \n3.- Mostrar productos \n4.- Salir \n"))
        match op:
            case 1:
                agregar()
            case 2:
                eliminar()
            case 3:
                mostrar()
            case 4:
                break
            case _:
                print("Error. Seleccione una opción válida")
    except Exception:
        print("Error. Solo debe ingresar números enteros.")