lista1 = []
lista2 = []

lista1.append("Oscar")

print(lista1)

lista1.append("Dominick")
print(lista1)

lista1.append("Max")
print(lista1)

lista1.append("Antonio")
print(lista1)

lista1.insert(1, "Freddy")
print(lista1)

lista1.insert(4, "Jorge")
print(lista1)

lista2 = lista1

print(f"lista 2 {lista2}")
print(f"lista 1 {lista1}")

lista1.append("Supermegarecontra")

print(f"lista 2 {lista2}")
print(f"lista 1 {lista1}")

lista1.pop()
print(f"lista 2 {lista2}")
print(f"lista 1 {lista1}")

#Eliminar el primer elemento
del lista1[0]
print(f"lista 2 {lista2}")
print(f"lista 1 {lista1}")

lista1.remove("Freddy")
print(f"lista 2 {lista2}")
print(f"lista 1 {lista1}")

lista1 = [name for name in lista1 if name != "Freddy"]

print(f"lista 2 {lista2}")
print(f"lista 1 {lista1}")