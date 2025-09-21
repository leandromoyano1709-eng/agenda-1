from controller.controlador import ejecutar_opcion
from view.vista import main_menu

def main():
    while True:
        opcion = main_menu()
        if opcion == "5":
            print("¡gracias por usar la agenda!")
            break 
        ejecutar_opcion(opcion)

if __name__ == "__main__":
      main()
