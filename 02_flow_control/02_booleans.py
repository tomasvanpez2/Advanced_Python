import os


os.system("clear")


print("\noperadores de comparación:")
print("\n==: Igual")
print("\n!=: Diferente")
print("\n<: Menor que")
print("\n<=: Menor o igual que")
print("\n> : Mayor que")
print("\n>=: Mayor o igual que")


print("\nComparación de cadenas:")

print("Ave > Perro:", "Ave" > "Perro")
#la comparación de cadenas se forman como un diccionario


print("\nTablas de verdad:")
print("\nand:")
print("A     B     A and B")
print("True  True ", True and True)
print("True  False", True and False)
print("False True ", False and True)
print("False False", False and False)

print("\n or:")
print("A     B     A or B")
print("True  True ", True or True)
print("True  False", True or False)
print("False True ", False or True)
print("False False", False or False)

print("\n not:") 
print("A     not A")
print("True ", not True)
print("False", not False)