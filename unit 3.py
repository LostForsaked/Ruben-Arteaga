# listas, diccionarios, set, tuplas son los tipos de colecciones

# crud = create, read, update and delete

mi_lista = [1,2,3,4,5]
for e in mi_lista:
    print(e)
########################
print(mi_lista[2])
########################
mi_lista.append(6)
for e in mi_lista:
    print(e)
########################
mi_lista.insert(3,"Juan")
for e in mi_lista:
    print(e)
########################
mi_lista = [1,2,3,"Juan",4,5]
mi_lista.remove("Juan")
#######################
mi_lista.pop(1)
#######################
mi_lista = [1,2,3,"Juan",4,5]
mi_lista.reverse() #invierte
mi_lista.sort() #ordena
#######################


