# pikachuroll=0
# otakuroll=0
# pulporoll=0
# anguilaroll=0
# op=0
# total=0
# subtotal=0
# descuento=0
# productos=0 


# while True:
#     while True:
#         try:
#             # print("Seleccione una opción: \n1.- Agregar Productos \n2.- Generar Boleta \n3.- Salir")
#             op=int(input("Seleccione una opción: \n1.- Agregar Productos \n2.- Generar Boleta \n3.- Salir \n"))
#         except Exception:
#             print("Seleccione sólo números enteros enlistados")
#         else:
#             break
# # while True:
#     match op:
#         case 1:
#             while True:
#                 while True:
#                     try:
#                         # print("Seleccione un producto: \n1.- Pikachu-Roll - $4500 \n2.- Otaku-Roll - $5000 \n3.-Pulpo Venenoso-Roll - $5200 \n4.- Anguila Eléctrica-Roll - $4800 \n 5.- Salir \n")
#                         prod=int(input("Seleccione un producto: \n1.- Pikachu-Roll - $4500 \n2.- Otaku-Roll - $5000 \n3.-Pulpo Venenoso-Roll - $5200 \n4.- Anguila Eléctrica-Roll - $4800 \n 5.- Salir \n"))
#                     except Exception:
#                         print("Seleccione sólo números enteros enlistados")
#                     else:
#                         break              
#             # while True:
#                 match prod:
#                     case 1:
#                         pikachuroll+=1
#                         subtotal=subtotal+4500
#                         productos+=1
#                     case 2:
#                         otakuroll+=1
#                         subtotal=subtotal+5000
#                         productos+=1
#                     case 3:
#                         pulporoll+=1
#                         subtotal=subtotal+5200
#                         productos+=1
#                     case 4:
#                         anguilaroll+=1
#                         subtotal=subtotal+4800
#                         productos+=1
#                     case 5:
#                         break
#                     case _:
#                         print("Seleccione una opción válida")
#         case 2:
#             while True:
#                 try:
#                     dcto=int(input("Tíene código de descuento? (1.- Si / 2.- no) \n"))
#                 except Exception:
#                     print("Ingrese sólo números enteros enlistados")
#                 else:
#                     break
#                 if dcto<=2:
#                     break
#                 else:
#                     print("Ingrese una opción válida")
#             if dcto==1:
#                 while True:
#                     cod=input("Ingrese el código de descuento")
#                     if cod=="soyotaku":

#                         descuento=subtotal*0.10
#                         total=subtotal-descuento
#                         break
#                     else:
#                         print("Codigo vencio o inválido")
#                         des=input("para intentarlo nuevamente presione 1, para salir presione x")
#                         if des=="x":
#                             break
#             print(f'''
#                     *******************************
#                     Total Productos: {productos}
#                     *******************************
#                     Pikachu Roll: {pikachuroll}
#                     Otaku Roll: {otakuroll}
#                     Pulpo Venenoso-Roll: {pulporoll}
#                     Anguila Eléctrica Roll: {anguilaroll}
#                     *******************************
#                     Subtotal por pagar: {subtotal}
#                     Descuento por código: {descuento}
#                     Total: {total}''')
#             decision=int(input("1.- Hacer otro pedido \n2.- Salir del programa \n"))
#         case 3:
#             break
#         case _:
#             print("Ingrese una opción válida")
###############################################################################################
# deuda=100000
# def tarjeta():
#     global deuda
#     deuda=100000
#     while True:
#         while True:
#             try:
#                 monto=int(input("Cuánto desea pagar? \n"))
#             except Exception:
#                 print("Ingrese sólo números enteros")
#             else:
#                 break
#         if monto>=0 and monto<=deuda:
#             deuda=deuda-monto
#         else:
#             print("Monto inválido")
#         print(f"Deuda actualizada, su deuda actual es de {deuda}")
#         choice=input("Para continuar presione Enter, para salir pulse X \n")
#         if choice=="x" or choice=="X":
#             break
# def sim():
#     total=0
#     while True:
#         while True:
#             try:
#                 monto=int(input("Ingrese el monto de la compra \n"))
#             except Exception:
#                 print("Ingrese el monto sin puntos y en números enteros")
#             else:
#                 break
#         if monto>=0:
#             total=total+monto
#         else:
#             print("Monto inválido")
#         print(f"El total acumulado de su simulación es de {total+deuda}")
#         choice=input("Para continuar pulse Enter. Si desea salir, pulse X")
#         if choice=="x" or choice=="X":
#             break
# while True:
#     while True:
#         try:
#             op=int(input("Seleccione una opción: \n1.- Pago Tarjeta \n2.- Simulación Compra \n3.- Salir \n"))
#         except Exception:
#             print("Solo ingrese números enteros")
#         else:
#             break
#     match op:
#         case 1:
#             tarjeta()
#         case 2:
#             sim()
#         case 3:
#             break
#         case _:
#             print("Seleccione una opción válida")



