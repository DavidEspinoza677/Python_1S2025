from datetime import date, datetime

print(date.today())
print(datetime.now())


class Solicitud:
    def __init__(self, nombre, asunto, carrera, siguiente=None):
        self.nombre = nombre
        self.siguiente = None
        self.asunto = asunto
        self.carrera = carrera
        self.siguiente = siguiente

    def __str__(self):
        return f"Estudiante: {self.nombre},  Asunto: {self.asunto}, Carrera: {self.carrera}"
    {self.carrera} ->

    def