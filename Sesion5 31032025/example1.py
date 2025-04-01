#Leer cantidad de edad y calcular la media 
import statistics
class Edad:
    def __init__(self, edad):
        self.edad = edad

    def calcular_media(self):
        return sum(self.edad) / len(self.edad)
    
    def mostrar_media(self):
        media = self.calcular_media()
        return f"La media de las edades es: {media:.2f} años"
    
    def calcular_media(self):
        return st.mean(self.edades)
    
def main():
    edades = []
    while True:
        try:
            edad = int(input("Ingrese la edad (o -1 para terminar): "))
            if edad == -1:
                break
            edades.append(edad)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    if(not edades):
        print("No se ingresaron edades.")
        return
    else:
        edad_obj = Edad(edades)
        print(edad_obj.mostrar_media())
        print(f"La media calculada es statistics: {edad_obj.calcular_media():.2f}")

    if __name__ == "__main__":
        main()