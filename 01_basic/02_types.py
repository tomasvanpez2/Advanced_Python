#tengo varios tipos de datos

# int, float, complex, str, bool, NoneType, list, tuple, dict, range, set


#los int son numeros enteros

print("int:")
print("10")
print("0")
print("15")

#se imprime en la terminal el tipo de dato

print("10",type(10))


#tambien estan los float que son decimales

print("float:")

print("1.0", type(1.0))
print("3.14", type(3.14))
print("1e3", type(1e3))

#hay otro tipo de datos que sirven para notación cientifica: los complex

print("1 + 2j",type(1 + 2j))


#los str son las cadenas de texto

print("hola", type("hola"))

print(" ", type(" ")) #los espacios tambien se cuentan como un str

print(type("123"))

#tambien estan los booleanos: bool

print("bool:")

print("True", type(True))
print("False", type(False))

print(1 > 2) #siempre va a responder un booleano.

#estan los NoneType estos son los que tienen ausencia de valor

print("NoneType:")

print("None", type(None))