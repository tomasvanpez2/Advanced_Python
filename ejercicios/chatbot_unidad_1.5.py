import os

os.system("clear")

print("Hola👋, soy tu asistente para encontrar tu carro perfecto. Puedes darme tu nombre")
nombre = input()

print(f'Hola {nombre}, ¿Para cuantas personas necesitas el carro?')
cantidad = input()

if cantidad <= "5":
    print("dame el numero de dias que necesitas el carro")
    dias = input()
    print(f"Perfecto, para {cantidad} personas y {dias} días, te recomiendo un carro tipo sedán, indicame tu presupuesto")
    presupuesto = input()
    if int(presupuesto) <= 200000:
        print("Te recomiendo el mitsubishi mirage, un carro económico y confortable")
    elif int(presupuesto) <= 150000:
        print("Te recomiendo el chevrolet spark, un carro estable y perfecto para tu presupuesto")
else:
    print("Si buscas un carro para más de 5 personas, te recomiendo una camioneta, ¿me puedes indicar tu presupuesto?")
    presupuesto_camioneta = input()
    if int(presupuesto_camioneta) <= 500000:
        print("Te recomiendo la Mitsubishi Montero, una camioneta espaciosa y cómoda")
    elif int(presupuesto_camioneta) <= 300000:
        print("Te recomiendo la Toyota Hilux, una camioneta resistente y confiable")
    else:
        print("Te recomiendo la Ford Ranger, una camioneta potente y versátil")
print("Gracias por usar nuestro servicio, ¡espero que encuentres el carro perfecto!")