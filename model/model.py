contacts = []

def search(n:str):
    for c in contacts:
        if c["name"]==n:
            return c

    return None

def insert(c):
    if search(c["name"]) is not None: return None
    
    contacts.append(c)
    return c

def delete(n:str):
    c = search(n)
    if c is None: return None

    contacts.remove(c)
    return c