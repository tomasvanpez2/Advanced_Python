###
# casting de tipos: trasformar un tipo de valor a otro
###




print(type("100"))

### 
# para convertir se usa:
###


print(type(int("100")))

#print(2 + "100") 
# #no se puede mezclar un entero con un string

###
#  pero si lo hago con la conversión si va a funcionar
###

print(2 + int("100"))

print(type(3.1416))


print(int(3.9416)) # solo quita el decimal 3.1416 se convierte en 3, pero 3,9416 da 3.
#solo quita el decimal


print(bool(1))
print(bool(0))
print(bool(-1))

### 
# todos los números a excepción del 0 seran "True" si se convierten a booleano
###


print(bool("")) #solo se convierte en False la cadena de texto vacia
print(bool("  "))
print(bool("False"))


### 
# como la funcion de convertir un decimal en un entero solo elimina el decimal 
# hay otra función para redondear
###

print(round(2.5)) #este funciona por aproximación
#pero si esta en un número intermedio entre dos numero 2, 3, 4
# el va a ir al par mas cercano, asi:

print(round(3.5))