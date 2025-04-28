import tkinter as tk
from tkinter import messagebox

class Pila:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add(self, item):
        self.items.append(item)

    def remove(self):
        if not self.is_empty():
            return f"Elemento eliminado: {self.items.pop()}"
        else:
            return "La pila está vacía, no se puede eliminar."

    def inspect(self):
        if not self.is_empty():
            return f"Elemento en la cima: {self.items[-1]}"
        else:
            return "La pila está vacía."

    def size(self):
        return len(self.items)

class PilaApp:
    def __init__(self, root):
        self.pila = Pila()
        self.root = root
        self.root.title("Administrador de Pila")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.setup_widgets()

    def setup_widgets(self):
        # Título
        title = tk.Label(self.root, text="Administrador de Pila", font=("Helvetica", 18))
        title.pack(pady=10)

        # Frame de entrada
        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=10)

        self.entry_add = tk.Entry(entry_frame, width=25)
        self.entry_add.pack(side=tk.LEFT, padx=5)

        self.btn_add = tk.Button(entry_frame, text="Agregar", command=self.add_item)
        self.btn_add.pack(side=tk.LEFT, padx=5)

        # Listbox para mostrar la pila
        self.listbox = tk.Listbox(self.root, width=40, height=10)
        self.listbox.pack(pady=10)

        # Frame de botones de acciones
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.btn_remove = tk.Button(button_frame, text="Eliminar Último", width=15, command=self.remove_item)
        self.btn_remove.grid(row=0, column=0, padx=5, pady=5)

        self.btn_inspect = tk.Button(button_frame, text="Inspeccionar Cima", width=15, command=self.inspect_item)
        self.btn_inspect.grid(row=0, column=1, padx=5, pady=5)

        self.btn_is_empty = tk.Button(button_frame, text="¿Está Vacía?", width=15, command=self.check_empty)
        self.btn_is_empty.grid(row=1, column=0, padx=5, pady=5)

        self.btn_size = tk.Button(button_frame, text="Tamaño", width=15, command=self.get_size)
        self.btn_size.grid(row=1, column=1, padx=5, pady=5)

        # Botón de salir
        self.btn_exit = tk.Button(self.root, text="Salir", command=self.root.quit, bg="red", fg="white")
        self.btn_exit.pack(pady=10)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for item in reversed(self.pila.items):
            self.listbox.insert(tk.END, item)

    def add_item(self):
        item = self.entry_add.get()
        if item:
            self.pila.add(item)
            self.update_listbox()
            self.entry_add.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un elemento.")

    def remove_item(self):
        result = self.pila.remove()
        self.update_listbox()
        messagebox.showinfo("Eliminar", result)

    def inspect_item(self):
        result = self.pila.inspect()
        messagebox.showinfo("Inspeccionar", result)

    def check_empty(self):
        empty = self.pila.is_empty()
        mensaje = "La pila está vacía." if empty else "La pila contiene elementos."
        messagebox.showinfo("¿Vacía?", mensaje)

    def get_size(self):
        size = self.pila.size()
        messagebox.showinfo("Tamaño", f"Número de elementos en la pila: {size}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PilaApp(root)
    root.mainloop()
