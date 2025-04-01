import example1

def main():
    edades = [3, 5, 7, 8, 9, 10]
    edad_obj = example1.Edad(edades)
    print(edad_obj.mostrar_media())

if __name__ == "__main__":
    main()