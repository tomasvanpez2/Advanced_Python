

age = 13

if age >= 18:
    print("Eres mayor de edad")
##esta es la forma mas basica de un if

### 
# pero tambien podemos hacer un if con else, que significa, si se 
# cumple la condición se ejecuta "", si no se ejecuta ""
###


if age >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


###
# si un profesar tiene notas es mas simple usando elif
###

nota = 3.5

if nota >= 5:
    print("Sobresaliente")
elif nota >= 4.5:
    print("Increíble")
elif nota >= 4:
    print("Notable")
elif nota >= 3.5:
    print("casi pierdes")
else:
    print("Reprobado")