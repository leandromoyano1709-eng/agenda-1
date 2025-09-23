from model import model as modelo
from view.vista import add_contact_menu

def agregar_contacts(nombre, telefono, email=""):
    return modelo.insert({
        "name": nombre,
        "phone": telefono,
        "email": email
    })

def lista_contacts():
   return modelo.get_all()

def buscar_contacts(nombre):
   return modelo.search(nombre)

def eliminar_contacts(nombre):
   return modelo.delete(nombre)

def ejecutar_opcion(opcion):
    if opcion == "1":
        c = add_contact_menu()
        agregar_contacts(c["name"], c["phone"])

        print("contacto agregado!")
    elif opcion == "2":
        contactos = lista_contacts()
        if not contactos:
            print("no hay contactos")
        else:
            for c in contactos:
                print(f"{c['name']} - {c['phone']}")
    elif opcion == "3":
        print("funcion editar en contruccion...")
    elif opcion == "4":
        nombre = input("ingrese el nombre a eliminar: ")
        eliminado = eliminar_contacts(nombre)
        if eliminado:
            print("contacto eliminado")
        else:
            print("no se encontro ese contacto.")
    else:
        print("opcion no valida")







