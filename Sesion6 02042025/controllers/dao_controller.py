

class MateriaDao:
    def __init__(self):
        self.materias = []  # Lista para almacenar las materias

    def agregar_materia(self, materia):
        self.materias.append(materia)  # Agregar materia a la lista

    def obtener_materias(self):
        return self.materias  # Retornar la lista de materias
    