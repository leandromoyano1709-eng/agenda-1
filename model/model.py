contacts = []
contact_id = "nombre"
campos = {contact_id:None,"tel":None,"dirección":None}

def search(n:str):
    for c in contacts:
        if c[contact_id].lower()==n.lower():
            return c

    return None

def insert(c: dict):
    if search(c[contact_id]) is not None: return None
    
    contacts.append(c)
    return c

def delete(n:str):
    c = search(n)
    if c is None: return None

    contacts.remove(c)
    return c

def update(n: str, new_data: dict):
    c = search(n)
    if c is None:
        return None 
    c.update(new_data)
    return c

def get_all():
    return contacts

    return c

def get_all():
    return contacts
