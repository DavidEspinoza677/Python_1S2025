import models.clases as c

class Promedio:
    def __init__(self):
        self._notas = []

    def agregar_nota(self, nota):
        self._notas.append(nota)
        
    def calcular_promedio(self):
        suma = 0
        for nota in self._notas:
            suma = nota.nota
        return suma / len(self._notas)
    
die = Estudiante("d" , "d" , "a" , "i")
print(die)

