###
#print("\nEjercicio 1: Imprimir mensajes")
#print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")
###

print("Hola!, ¿Como te llamas?")
name = input()
print(f"Perfecto {name}, ¿En qué ciudad vives?")
city = input()
print(f"Gracias {name}, vives en {city}")

print("------------------------------------------")
#completado


###
#print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
#print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("-------------------------------------------")
#completado


###
#print("\nEjercicio 3: Casting de tipos")
#print("Convierte la cadena \"12345\" a un entero y luego a un float.")
#print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

cadena = "12345"
float = 3.99

print(int(cadena)) 
print(int(float))


print("----------------------------------------")
#completado




#print("\nEjercicio 4: Variables")
#print("Crea variables para tu nombre, edad y altura.")
#print("Usa f-strings para imprimir una presentación.")



nombre = input("¿cual es tu nombre?")
edad = 13
altura = 1.60

print(f"Hola! Me llamo {nombre} y tengo {edad} años, mido {altura} metros")




print("------------------------------------------------------------")

#print("\nEjercicio 5: Números")
#print("1. Crea una variable con el número PI (sin asignar una variable)")
#print("2. Redondea el número con round()")
#print("3. Haz la división entera entre el número que te salió y el número 2")
#print("4. El resultado debería ser 1")

pi = 3.14159
print(round(pi))
resultado = round(pi)
print(resultado)
print(resultado // 2)  