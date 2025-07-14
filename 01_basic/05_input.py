# Entrada del usuario: Cuando se llama a input().
# el programa se detiene y espera a que el usuario escriba algo seguido de presionar Enter.

print("¿Cuál es tu nombre?")
name = input()

print(f"Hola {name}, me puedes dar tu número de telefono?")
phone_number = input()
print(f"Gracias {name}, tu número de telefono es {phone_number}")
print("¿Cuántos años tienes?")
age = input()
age = int(age)  # Cast - str a int

print(f"Gracias {name}, en 20 años tendrás {age + 20} años")
#la expresión age + 20 no es correcta porque aunque visualmente se vea un numero es un string

print("en que ciudad y pais vives?")
city, country = input().split()

print(f"Gracias {name}, vives en {city}, {country}")