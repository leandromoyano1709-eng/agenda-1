from model import model as modelo
from view import view as vista

def agregar_contacto(c):
    return modelo.insert(c)

def lista_contacto():
   return modelo.get_all()

def buscar_contacto(nombre):
   return modelo.search(nombre)

def eliminar_contacto(nombre):
   return modelo.delete(nombre)

def ejecutar_opcion(opcion):
    if opcion == "1":
        c = vista.add_contact_menu(modelo.campos)
        agregar_contacto(c)

        print("contacto agregado!")
    elif opcion == "2":
        contactos = lista_contacto()
        vista.list_contacts(contactos)
    elif opcion == "3":
        print("funcion editar en contruccion...")
    elif opcion == "4":
        nombre = input("ingrese el nombre a eliminar: ")
        eliminado = eliminar_contacto(nombre)
        if eliminado:
            print("contacto eliminado")
        else:
            print("no se encontro ese contacto.")
    else:
        print("opcion no valida")

def main_loop():
    while True:
        opcion = vista.main_menu()
        if opcion == "5":
            print("¡gracias por usar la agenda!")
            break 
        ejecutar_opcion(opcion)









