import model

def agregar_contacts(nombre, telefono, email):
    return modelo.insert({
        "name": nombre
        "phone": telefono,
        "email": email
    })

def lista_contacts():
   return model.get_all()

def buscar_contacts(nombre):
   return model.search(nombre)

def eliminar_contacts(nombre):
   return model,delete(nombre)

def actualizar_contacts(nombre, telefono=None, email=None):
    nuevos_datos = {}
    if telefono:
        new_data["phone"] = telefono 
    if email:
        new_data["email"] = email
    return model.update(nombre, nuevos_datos)

