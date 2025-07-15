import os

os.system("clear")

print("dame tu edad")
edad = int(input())

if edad <= 2:
    print("Eres un bebé")
elif edad <= 11:
    print("Eres un niño")
elif edad <= 17:
    print("Eres un adolescente")
elif edad <= 70:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")