#   Agregar los nombres de x cantidad de estudiates 

list_students = list()

def add_stuednt():
    student = input("ingresa el nombre del estudiante: ")
    list_students.append(student)

def show_students():
    print(list_students)
    for students in list_students:
        print(students)

while True:
    add_stuednt()
    show_students()
    if input("Deseas agregar otro estudiante? (s/n): ").lower() != "s":
        break

print("Gracias por usar el programa")
