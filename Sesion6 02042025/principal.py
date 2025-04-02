import models.clases as c
import controllers.dao_controller as dao
import os




materia = c.Materia("Calculo", "MAT101", 4)

materia_dao = dao.MateriaDao()
materia_dao.agregar_materia(materia)
materias = materia_dao.obtener_materias()
print(materias[0])  # Imprimir la primera materia de la lista