
class Directory:
    def __init__(self):
        self.rubrica = []

    def __len__(self):
        return len(self.rubrica)

    def add(self, contatto):
        self.rubrica.append(contatto)

    def query(self, name):
        return [contact for contact in self.rubrica if contact.name == name]

    def find(self, param):
        return [contact for contact in self.rubrica
                if param in contact.name or
                hasattr(contact,"surname") and param in contact.surname or
                (contact.phone and param in contact.phone)]

class Person:
    def __init__(self, name, surname, phone = None):
        self.name = name
        self.surname = surname
        self.phone = phone

class Business:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

