#Almacenar un listado de estudiante, calcular su promedio de n clases

#Clases basicas o modelos 

class Asignatura:
    def __init__(self, nombre, descripcion, credito):
        self.nombre = nombre
        self.descripcion = descripcion
        self.credito = credito

    def __str__(self):
        return f"""asignatura {'{'} "nombre" :{'{'} "{self.nombre}" , "descripcion": "{self.
        descripcion}, "credito", "credito" : {self.credito} {'}'}""" 

class Estudiante:
    def __init__(self, cif, nombre, apellido, carrera):
        self.cif = cif
        self.nombre = nombre
        self.apellido = apellido
        self.carrera = carrera

    def __str__(self):
        return f"""estudiante {self.cif} {self.nombre} {self.apellido} {self.carrera}"""

class Nota:
    def __init__(self, estudiantes, asignatura, nota):
        self.estudiantes = estudiantes
        self.asignatura = asignatura
        self.nota = nota

    def __str__(self):
        return
    



asig = Asignatura("POO", "POO...", 3)
print(asig)