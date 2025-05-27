 # Explicacion y uso de match

# def suma():
#     n1=int(input("Ingrese un número: "))
#     n2=int(input("Ingrese otro número: "))
#     print(f"El resultado de la suma es {n1+n2}")
# def resta():
#     n1=int(input("Ingrese un número: "))
#     n2=int(input("Ingrese otro número: "))
#     print(f"El resultado de la resta es {n1-n2}")
# def multiplicacion():
#     n1=int(input("Ingrese un número: "))
#     n2=int(input("Ingrese otro número: "))
#     print(f"El resultado de la multiplicacion es {n1*n2}")
# def division():
#     try:
#         n1=int(input("Ingrese un número: "))
#         n2=int(input("Ingrese otro número: "))
#         print(f"El resultado de la division es {n1/n2}")
#     except ZeroDivisionError as nombre_de_excepcion:
#         print(f"Se produjo una excepción {nombre_de_excepcion}")

# def calcu():

#     while True:
#         op=int(input('''Seleccione su opción
#                     1.- suma
#                     2.- resta
#                     3.- multiplicacion
#                     4.- division
#                     5.- salir
#                     '''))

#         match op:
#             case 1:
#                 print("suma")
#                 suma()
#             case 2:    
#                 print("resta")
#                 resta()
#             case 3:    
#                 print("multiplicacion")
#                 multiplicacion()
#             case 4:
#                 print("Division")
#                 division()
#             case 5:
#                 break
#             case _:
#                 print("Opción inválida")

# def mayor_que():
#     n1=int(input("Ingrese un primer número \n"))
#     n2=int(input("Ingrese un segundo número \n"))
#     n3=int(input("Ingrese un tercer número \n"))
#     if n1>n2 and n1>n3:
#         print(f"El número mayor es {n1}")
#     elif n2>n1 and n2>n3:
#         print(f"El número mayor es {n2}")
#     else:
#         print(f"El número mayor es {n3}")

# def edades():

#     edad=int(input("Ingrese su edad \n"))
#     if edad>0 and edad<13:
#         print("Usted es un niño")
#     elif edad>=13 and edad<17:
#         print("Usted es un adolescente")
#     else:
#         print("Usted es un adulto")

# while True:
#     print("Seleccione un programa \n1.- calculadora \n2.- Número mayor \n3.- Edades \n4.- Salir")
#     opcion=int(input())
#     match opcion:
#         case 1:
#             print("Calculadora")
#             calcu()
#         case 2:
#             print("Numero mayor")
#             mayor_que() 
#         case 3:
#             print("Edades")
#             edades()
#         case 4:
#             print("Salir")
#             break
#         case _:
#             print("Opcion inválida")



# while True:
#     try:
#         num=int(input("Ingrese un número mayor que 3 \n "))
#         if num>3:
#             break
#     except Exception:
#         print("Solo debe ingresar números, no texto")

import os
import time
# os.system('cls') #para limpiar la pantalla
total=0
articulos=0
productos=0
while True:
    try:
        op=int(input("Seleccione una opción: \n1.- Ingresar nombre de usuario \n2.- Comprar \n3.- Generar boleta \n4.- Salir \n"))
        os.system('cls')
        time.sleep(0.5)
    except Exception:
        print("Seleccione números solamente")
    match op:
        case 1:
            user=str(input("Ingrese su nombre de usuario \n"))
            os.system('cls')
            time.sleep(0.5)
        case 2:
            while True:
                try:
                    productos=int(input("Seleccione un producto: \n1.- The Last Of Us PS5 - $69990 \n2.- Control Dualsense - $79990 \n3.- God Of War Ragnarok PS5 - $69990 \n4.- Assassin's Creed Shadows PS5 - $69990 \n5.- EA FC25 PS5 - $69990 \n6.- Consola PS5 - 650000 \n7.- Salir \n"))
                except Exception:
                    print("Por favor, solamente ingrese uno de los números en el menú")
                match productos:
                    case 1:
                        total=total+69990
                        articulos+=1
                        os.system('cls')
                        time.sleep(0.5)
                    case 2:
                        total=total+79990
                        articulos+=1
                        os.system('cls')
                        time.sleep(0.5)
                    case 3:
                        total=total+69990
                        articulos+=1
                        os.system('cls')
                        time.sleep(0.5)
                    case 4:
                        total=total+69990
                        articulos+=1
                        os.system('cls')
                        time.sleep(0.5)
                    case 5:
                        total=total+69990
                        articulos+=1
                        os.system('cls')
                        time.sleep(0.5)
                    case 6:
                        total=total+650000
                        articulos+=1
                        os.system('cls')
                        time.sleep(0.5)
                    case 7:
                            os.system('cls')
                            time.sleep(0.5)
                            break
                    case _:
                        print("Seleccione una opción válida")
        case 3:
            os.system('cls')
            time.sleep(0.5)
            print(f"Usted lleva un total de {articulos} productos")
            print(f"El total neto de su compra es de ${total}")
            print(f"El total de su compra mas IVA agregado es de ${total*1.19}")
            print(f"Muchas gracias por su compra {user}")
            print("Vuelva pronto")
        case 4:
            os.system('cls')
            time.sleep(0.5)
            print("Saliendo del sistema")
            break
        case _:
            time.sleep(0.5)
            print("Seleccione una opción válida")



#para cerrar un programa desde un submenu hay que importar sys y luego escribir sys.exit()