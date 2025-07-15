import os
os.system("clear")

print("\nCrear Listas:")
Lista1 = [1, 2, 3, 4, 5] # Lista de enteros

Lista2 = ["a", "b", "c"] # Lista de cadenas

Lista3 = [1, "a", True, 3.14] # Lista mixta

Lista_de_listas = ["pera", "manzana"], ["uva", "kiwi"] # Lista de listas



print(Lista1)
print(Lista2)
print(Lista3)


#para acceder a un elemento de una lista:
print("\nAcceder a elementos de una lista:")

print(Lista1[0]) # Primer elemento

#para acceder a lista de listas:

print(Lista_de_listas[0][0]) # Pera

#para obtener solamente 1 indice:

lista_slicing = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\nObtener un índice específico de una lista:")
print(lista_slicing[1:5]) #obtiene desde el 2 hasta el #5 (el valor 5 en la lista no se incluye)

#hay otra forma en la cual se pasan ciertos numeros:

print("\nObtener elementos con 'paso':")
print(lista_slicing[::2]) # va a saltar de 2 en 2


#modificar una lista

lista_modificar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

lista_modificar[0] = 0 # cambio el valor con el elemento 1 que esta en la posicion 0 a un "0"

print(lista_modificar)

#agregar un elemento a una lista


#forma mas larga y poco eficiente
lista_modificar = lista_modificar + [16, 17, 18]

#forma mas corta y eficiente
lista_modificar += [19, 20, 21]
print(lista_modificar)