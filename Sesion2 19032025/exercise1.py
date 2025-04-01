nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
if edad >=0 and edad <= 12:
    print(nombre + " es un niño")
elif edad >=13 and edad <= 17:
    print(nombre + " es un adolescente")
elif edad >=18 and edad <= 29:
    print(nombre + " es un joven")
elif edad >=30 and edad <= 59:
    print(nombre + " es un adulto")
elif edad >=60:
    print(nombre + " es un adulto mayor")