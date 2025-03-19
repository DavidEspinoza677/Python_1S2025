cont = 1 
number = int(input("Ingrese un número: "))
print(f"tabla de multiplicar del {number}")
print ("="*13)
while cont <= 12:
 print(f"{cont}*{cont}={cont*cont}")
 cont += 1
print("="*13)