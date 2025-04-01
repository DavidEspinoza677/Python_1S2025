#listas divididas 
#1. Pilas 
#2. Colas - Filas 

#Pilas:

stack = []

def push(val):
    if len (stack) < 5:
       stack.append(val)
    else:
        print("Stack Overflow")


def pop():
    if len(stack) > 0:
        return stack.pop()
    else:
        print("Stack Underflow")

def menu():
    print("1. Push")
    print("2. Pop")
    print("3. Exit")
    return int(input("Selecciona una opcion: "))

while True:
    option = menu()
    if option == 1:
        push(int(input("Ingresa un valor: ")))
    elif option == 2:
        print(pop())
    elif option == 3:
        break
    else:
        print("Opcion invalida")

