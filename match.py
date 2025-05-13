 # Explicacion y uso de match

def suma():
    n1=int(input("Ingrese un número: "))
    n2=int(input("Ingrese otro número: "))
    print(f"El resultado de la suma es {n1+n2}")
def resta():
    n1=int(input("Ingrese un número: "))
    n2=int(input("Ingrese otro número: "))
    print(f"El resultado de la resta es {n1-n2}")
def multiplicacion():
    n1=int(input("Ingrese un número: "))
    n2=int(input("Ingrese otro número: "))
    print(f"El resultado de la multiplicacion es {n1*n2}")
def division():
    try:
        n1=int(input("Ingrese un número: "))
        n2=int(input("Ingrese otro número: "))
        print(f"El resultado de la division es {n1/n2}")
    except ZeroDivisionError as nombre_de_excepcion:
        print(f"Se produjo una excepción {nombre_de_excepcion}")

def calcu():

    while True:
        op=int(input('''Seleccione su opción
                    1.- suma
                    2.- resta
                    3.- multiplicacion
                    4.- division
                    5.- salir
                    '''))

        match op:
            case 1:
                print("suma")
                suma()
            case 2:    
                print("resta")
                resta()
            case 3:    
                print("multiplicacion")
                multiplicacion()
            case 4:
                print("Division")
                division()
            case 5:
                break
            case _:
                print("Opción inválida")

def mayor_que():
    n1=int(input("Ingrese un primer número \n"))
    n2=int(input("Ingrese un segundo número \n"))
    n3=int(input("Ingrese un tercer número \n"))
    if n1>n2 and n1>n3:
        print(f"El número mayor es {n1}")
    elif n2>n1 and n2>n3:
        print(f"El número mayor es {n2}")
    else:
        print(f"El número mayor es {n3}")

def edades():

    edad=int(input("Ingrese su edad \n"))
    if edad>0 and edad<13:
        print("Usted es un niño")
    elif edad>=13 and edad<17:
        print("Usted es un adolescente")
    else:
        print("Usted es un adulto")

while True:
    print("Seleccione un programa \n1.- calculadora \n2.- Número mayor \n3.- Edades \n4.- Salir")
    opcion=int(input())
    match opcion:
        case 1:
            print("Calculadora")
            calcu()
        case 2:
            print("Numero mayor")
            mayor_que() 
        case 3:
            print("Edades")
            edades()
        case 4:
            print("Salir")
            break
        case _:
            print("Opcion invlida")