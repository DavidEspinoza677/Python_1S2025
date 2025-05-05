from banco import Banco

def mostrar_menu():
    print("\n------ MENU DEL BANCO ---")
    print("1. Llegar cliente")
    print("2. Atender cliente")
    print("3. Mostrar clientes en espera")
    print("4. Salir")
    

def main():
    banco = Banco()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            cliente = input("Ingrese el nombre del cliente: ")
            banco.llegar_cliente(cliente)
            print(f"Cliente {cliente} ha llegado.")
        
        elif opcion == "2":
            cliente_atendido = banco.atender_cliente()
            if cliente_atendido:
                print(f"Atendiendo al cliente: {cliente_atendido}")
            else:
                print("No hay clientes en espera.")
        
        elif opcion == "3":
            clientes_en_espera = banco.obtener_clientes_en_espera()
            if clientes_en_espera:
                print("Clientes en espera:")
                for cliente in clientes_en_espera:
                    print(cliente)
            else:
                print("No hay clientes en espera.")
        
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()