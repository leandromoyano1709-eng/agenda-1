
def main_menu():
    print("--Menu Principal--")
    print("1.Agregar contacto")
    print("2.Listar contactos")
    print("3.Editar contacto")
    print("4.Eliminar contacto")
    print("5.Salir")

    return input("seleccione una opción: ")

def add_contact_menu(campos:dict):
    c = {}
    for key,value in campos.items():
        c[key] = input(key+" : ")

    return c

def list_contacts(l):
    if not l:
        print("No hay contactos registrados")
        return None

    campos = l[0].keys() # todos los campos del contacto

    columnas = {} # guarda el tamaño de cada columna
    for i in campos:
        columnas[i] = len(i)+1
    
    for contacto in l: #recorre cada contacto
        for campo in campos: #recorre cada campo para obtener informacion del contacto
            if len(contacto[campo])>columnas[campo]:
                columnas[campo]=len(contacto[campo])
    
    header = " | "
    for campo in campos:
        header=header+campo.upper().ljust(columnas[campo])+" | "
    print("-"*len(header))
    print(header)
    print("-"*len(header))

    for i in l:
        line = " | "
        for campo in campos:
            line=line+i[campo].ljust(columnas[campo])+" | "
        print(line)
    print("-"*len(header))
    