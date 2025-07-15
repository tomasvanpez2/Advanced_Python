import os
os.system("clear")


#añadir un elemento al final de la lista

lista1 = [1, 2, 3] 
lista1.append(4)
print(lista1)

#insertar un elemento en una posicion especifica

lista1 = ["a", "b", "c"]
lista1.append("d")
print(lista1)
lista1.insert(1, "@") #se inserta en la posicion 1 y dezplaza el resto a la derecha
print(lista1)

#insertar varios elementos al final de la lista

lista1.extend(["e", "f", "g"]) 
print(lista1)


#eliminar un elemento de la lista

lista1.remove("@") # elimina la primera aparición de el elemento "" en la lista
print(lista1) 

#eliminar el ultimo elemento de la lista y te lo devuelve

guardado_pop = lista1.pop()

print(lista1)
#print(guardado_pop) 

#eliminar rangos de elementos de la lista

print(lista1)
del lista1[4:] #se usa la misma sitaxis
print(lista1)

#ordenar listas

numbers = [5, 2, 9, 1, 4, 6, 3, 8, 7]
numbers.sort()
print(numbers)