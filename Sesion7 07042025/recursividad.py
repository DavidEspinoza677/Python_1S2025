# Factorial de un numero 
listFact = []
listFibo = []


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    
def fibonacci(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
    
# Ejemplo de uso de la función factorial
num = 5
resultado = factorial(num)
print(f"El factorial de {num} es: {resultado}")

# Ejemplo de uso de la función fibonacci
num = 6
resultado = fibonacci(num)
for i in range(num + 1):
    print(fibonacci(i), end = " ")

# Cargar listas de factoriales y fibonacci   
def cargarFactorial():
    for i in range(1, num + 1):
        listFact.append(factorial(i))
    return listFact

def cargarFibonacci():
    for i in range(1, num + 1):
        listFibo.append(fibonacci(i))
    return listFibo

class SerieFibo:
    def _init_(self, num = None, nodo = None):
        self.num = num
        self.nodo = nodo
    
    def _str_(self):
        return str(self.num)
        
    
class SerieFact:
    def _init_(self, num = None, nodo = None):
        self.num = num
        self.nodo = nodo
    
    def _str_(self):
        return str(self.num)

# Imprimir los resultados
def main():
    num = int(input("Ingrese un numero: "))
    listFa = []
    listFi = []
    
    for i in range(1, num + 1):
        sfi = SerieFibo(fibonacci(i))
        listFi.append(sfi)
        sfa = SerieFact(factorial(i))
        listFa.append(sfa)
    
    print("Lista de Fibonacci:")
    for i in listFi:
        print(i.num, end = " -> ")
    print("\nLista de Factorial:")
    for i in listFa:
        print(i.num, end = " -> ")
    print("None")