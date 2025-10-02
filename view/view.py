def main_menu():
    print("--Menu Principal--")
    print("1.Agregar contacto")
    print("2.Listar contactos")
    print("3.Editar contacto")
    print("4.Eliminar contacto")
    print("5.Salir")

    return input("seleccione una opción")

def add_contact_menu(campos:dict):
    c = {}
    for key,value in campos.items():
        c[key] = input(key+" : ")

    return c

def list_contacts(l):
    for i in l:
        print(i)