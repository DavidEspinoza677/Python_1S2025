import tkinter as tk

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def obtener_nodos(self):
        nodos = []
        actual = self.cabeza
        while actual:
            nodos.append(actual.dato)
            actual = actual.siguiente
        return nodos

    def graficar(self):
        nodos = self.obtener_nodos()
        ventana = tk.Tk()
        ventana.title("Visualización de Lista Enlazada")
        canvas = tk.Canvas(ventana, width=1000, height=200, bg="white")
        canvas.pack()
        x = 50
        for i, dato in enumerate(nodos):
            # Dibuja nodo
            canvas.create_rectangle(x, 50, x+100, 100, fill="lightblue")
            canvas.create_text(x+50, 75, text=dato)
            # Flecha
            if i < len(nodos) - 1:
                canvas.create_line(x+100, 75, x+120, 75, arrow=tk.LAST, width=2)
            x += 130
        ventana.mainloop()

# Ejemplo de uso
lista = ListaEnlazada()
"""for nombre in ["Fernando", "Roderick", "Allan", "Guillermo", "Diedereich", "David", "Elias"]:
    lista.agregar(nombre)
"""

def menu():
    print("1. Agregar nodo")
    print("2. Graficar lista")
    print("3. Salir")
    return int(input("Seleccione una opción: "))

while True:
    opcion = menu()
    if opcion == 1:
        nombre = input("Ingrese el nombre: ")
        lista.agregar(nombre)
    elif opcion == 2:
        lista.graficar()
    elif opcion == 3:
        break
    else:
        print("Opción no válida. Intente de nuevo.")

