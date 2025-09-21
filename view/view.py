def main_menu():
    print("--Menu Principal--")
    print("1.Agregar contacto")
    print("2.Listar contactos")
    print("3.Editar contacto")
    print("4.Eliminar contacto")
    print("5.Salir")

    return input("seleccione una opción")

def add_contact_menu():
    c = {}

    name = input("nombre : ")
    phone = input("tel : ")
    email = input("email (opcional) : ")
    c["name"] = name
    c["phone"] = phone
    c["email"] = email
    return c
