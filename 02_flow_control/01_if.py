###  
# vamos a empezar a importar lbrerias
# estas tienen funciones especificas
###


import os
os.system("clear")




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


tiene_licencia = True
edad = 18

if edad >= 16 and tiene_licencia:
    print("Puedes conducir🚘")
else:
    print("Policia👮🏼‍♀️")

#en otros casos:

if edad >= 16 or tiene_licencia:
    print("Puedes conducir🚘")
else:
    print("paga 150K de multa👮🏼‍♀️")


es_fin_de_semana = True

if not es_fin_de_semana:
    print("Es un día de semana, a trabajar💼")



# viendo el cast tambien pudimos determinar que se pueden evaluar diferentes tipos en booleanos

numero = 5 # en el cast vimos que todos los numeros que no sean 0 son True
if numero:
    print("El numero no es 0")


nombre = "Juan" # en el cast vimos que las cadenas de texto no vacias son True
if nombre:
    print("El nombre no esta vacio")