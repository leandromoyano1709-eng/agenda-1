contacts = []

def search(n:str):
    for c in contacts:
        if c["name"]==n:
            return c

    return None

def insert(c: Dict):
    if search(c["name"]) is not None: return None
    
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
