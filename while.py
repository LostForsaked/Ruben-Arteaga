# botella=600
# sed=True
import random
import time
# while botella>=0 and sed:
#     print("Glup, glup")
#     botella=botella-(random.randint(20,60))
#     print(f"Queda {botella}")
#     resp=input("Aún tiene sed? (si/no)")
#     if resp=="no":
#         sed=False
#     time.sleep(1)


# chocolate=1

# if chocolate==1:
#     print("Hay chocholate")
# else:
#     print("No hay chocholate")

# print("Salió GTA6? 1.- si, 0.- No")
# gta6=int(input())

# if gta6==1:
#     print("Gta6 Disponible")
# else:
#     print("Gta6 aún no está disponible")



# credito=0

# cant_ingresos=int(input("Cuánto es su ingreso mensual? "))

# if cant_ingresos>=500000 and cant_ingresos<=1000000:
#     credito=credito+300000
# elif cant_ingresos>=1000001 and cant_ingresos<=1500000:
#     credito=credito+650000
# else:
#     credito=credito+1000000

# nv_soc=int(input('''
#               Cuál es su nivel educacional?
#               1.- basico
#               2.- medio
#               3.- superior
#               '''))
# if nv_soc==1:
#     credito=credito
# elif nv_soc==2:
#     credito=credito+(credito*1.3)
# elif credito==3:
#     credito=credito+(credito*1.5)

# nac=input("Es usted chileno? (si/no)")
# if nac=="si":
#     credito=credito+300000
# else:
#     print("Que se vayan los venecos")

# print(f"Su credito es de {credito}")


parameter1=int(input("Ingrese un número "))
parameter2=int(input("Ingrese un segundo número (debe ser mayor que el primero)"))
while parameter2<parameter1:
    print("Debe ser mayor que el primero")
    parameter2=int(input("Ingrese un segundo número"))
rand_num=random.randint(parameter1,parameter2)
for i in range(rand_num):
    print("▄")

print(f"el ▄ fue impreso {rand_num} veces")


