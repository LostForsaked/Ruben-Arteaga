usuario1=None
usuario2=None
usuario3=None
contrasena1=None
contrasena2=None
contrasena3=None
mensaje=None
login=False
def inicio():
    global login
    while True:
        while True:
            try:
                user=input("Ingrese su nombre de usuario \n")
                break
            except Exception:
                print("Error. Intente nuevamente")
        if usuario1==None and usuario2==None and usuario3==None:
            print("No se encuentran usuarios registrados. Debe registrar usuarios para iniciar sesión.")
            break
        if user==usuario1:
            try:
                passwd=input("Ingrese su contraseña: \n")
                if passwd==contrasena1:
                    print("Sesión iniciada correctamente")
                    login=True
                    break
                else:
                    print("Contraseña incorrecta")
                    break
            except Exception:
                print("Error.")
        if user==usuario2:
            try:
                passwd=input("Ingrese su contraseña: \n")
                if passwd==contrasena2:
                    print("Sesión iniciada correctamente")
                    login=True
                    break
                else:
                    print("Contraseña incorrecta")
                    break
            except Exception:
                print("Error.")
        if user==usuario3:
            try:
                passwd=input("Ingrese su contraseña: \n")
                if passwd==contrasena3:
                    print("Sesión iniciada correctamente")
                    login=True
                    break
                else:
                    print("Contraseña incorrecta")
                    break
            except Exception:
                print("Error.")
def registro():
    global usuario1, usuario2, usuario3, contrasena1, contrasena2, contrasena3
    user=input("Ingrese el nombre de usuario a registrar: \n")
    if user==usuario1 or user==usuario2 or user==usuario3:
        print("El nombre de usuario se encuentra registrado")
    if usuario1==None and contrasena1==None:
        usuario1=user
        passwd1=input("Ingrese la contraseña \n")
        contrasena1=passwd1
    else:
        if usuario1!=None and usuario2==None:
            usuario2=user
            passwd2=input("Ingrese la contraseña")
            contrasena2=passwd2
        else:
            if usuario1!=None and usuario2!=None and usuario3==None:
                usuario3=user
                passwd3=input("Ingrese la contraseña")
                contrasena3=passwd3
def llamada():
    while True:
        while True:
            try:
                numero=input("Ingrese el número telefónico: \n")
                break
            except Exception:
                print("Sólo ingrese números enteros")
        if numero.isdigit():
            if  numero.startswith("9") and len(numero)==9:
                print("Llamada realizada")
                break
            else:
                print("Ingrese un número telefónico válido")
        else:
            print("Solo ingrese números enteros")
def correo():
    global mensaje
    while True:
        correo=input("Ingrese su correo electrónico: \n")
        if "@" in correo:
            mensaje=input("Ingrese su mensaje \n")
            print("Mensaje enviado")
            break
        else:
            print("Correo inválido")

while True:
    op=int(input("Seleccione una opción: \n1.- Iniciar Sesión \n2.- Registrarse \n3.- Salir \n"))
    match op:
        case 1:
            inicio()
            while login==True:
                while True:
                    try:
                        op2=int(input("Seleccione una opción: \n1.- Llamada \n2.- Email \n3.- Salir \n"))
                        break
                    except Exception:
                        print("Ingrese solo números enteros")
                match op2:
                    case 1:
                        llamada()
                    case 2:
                        correo()
                    case 3:
                        break
                    case _:
                        print("Seleccione una opción válida")
        case 2:
            registro()
        case 3:
            break
        case _:
            print("Seleccione una opción válida")