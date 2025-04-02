# Crear un registro de materias

class Materia:
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos

    def __str__(self):
        return f"Materia: {self.nombre}, Codigo: {self.codigo}, Creditos: {self.creditos}"
    