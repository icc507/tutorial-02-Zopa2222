#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)
lista1 = input().split()
lista2 = input().split()

lista = lista2+lista1+lista2

for i in range(0,len(lista)):
    if lista[i].isdigit():
        lista[i]=int(lista[i])

print(tuple(lista))
