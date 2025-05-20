import random
import time

# while True:
#     try:
#         cant_perros=int(input("Cuántos perros enviará? \n"))
#     except Exception:
#         print("Ingrese la cantidad en formato numérico")
#     else:
#         break
# while True:
#     try:
#         minimo=int(input("Ingrese la cuota mínima para la recompensa: \n"))
#     except Exception:
#         print("Ingrese la cantidad en formato numérico")
#     else:
#         break
# no=0
# si=0
# for i in range(cant_perros):
#     perro=random.randint(1,(minimo+5))
#     print(f"El perro n°{i+1} trajo {perro} conejos")
#     time.sleep(0.5)
#     if perro>=minimo:
#         print(f"El perro n°{i+1} recibe la recompensa")
#         time.sleep(0.5)
#         si=si+1
#     elif perro<minimo:
#         print(f"El perro n°{i+1} no recibe recompensa")
#         time.sleep(0.5)
#         no=no+1
# print("************************************************************")
# print(f"La cantidad de perros que recibieron recompensa es de {si}")
# time.sleep(0.5)
# print(f"La cantidad de perros que no recibieron recompensa es de {no}")
# time.sleep(0.5)

# rojos=int(input("Ingrese la cantidad de rojos en el curso: \n"))

# for i in range(rojos):
#     talleres=random.randint(1,4)
#     decimas=0.3*talleres
#     if decimas>=1:
#         bendicion=True
#     else:
#         bendicion=False
#     nota=float(input("Ingrese la nota: \n"))
#     nota_fin=nota+decimas
#     print(f"la nota final del alumno es {round(nota_fin,1)}")

#     if nota_fin>=3.5 and bendicion==True:
#         nota_fin=4.0
#     if nota_fin>=4:
#         print("El estudiante aprueba")
#     else:
#         print("El estudiante reprueba")
total=0
full=0
standard=0
basico=0
autos=0
while True:
    while True:
        try:
            op=int(input("Seleccione una opción: \n1.- Cursar pago del lavado \n2.- Ver ventas diarias \n3.- Salir \n"))
        except Exception:
            print("Ingrese solo numeros enteros")
        else:
            break
    match op:
        case 1:
            print("Cursar pago del lavado")
            while True:
                print("Seleccione el tipo de lavado")
                while True:
                    try:
                        
                        op1=int(input("1.- Full - $15.000 \n2.- Standard - $10.000 \n3.- Básico - $7.000 \n4.- Salir \n"))
                    except Exception:
                        print("Seleccione solo números enteros")
                    else:
                        break
                match op1:
                    case 1: 
                        print("Lavado Full - $15.000")
                        total=total+15000
                        autos=autos+1
                        full=full+1
                    case 2:
                        print("Lavado Standard - $10.000")
                        total=total+10000
                        autos=autos+1
                        standard=standard+1
                    case 3:
                        print("Lavado Basico - $7.000")
                        total=total+7000
                        autos=autos+1
                        basico=basico+1
                    case 4:
                        break
                    case _:
                        print("Seleccione una opcioón válida")
        case 2:
            print("Ver ventas diarias")
            print(f"El total de ventas es de {total}")
            print(f"La cantidad de autos que han ingresado es de {autos}")
            if full>=1:
                print("El monto más alto pagado es de 15000")
            elif standard>=1 :
                print("El monto más alto pagado es de 10000")
            elif basico>=1 :
                print("El monto más alto pagado es de 7000")
        case 3:
            break
        case _:
            print("Seleccione una opción válida")


