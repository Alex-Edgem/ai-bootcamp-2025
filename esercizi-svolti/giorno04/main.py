
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

directory = Directory()

assert len(directory) == 0

directory.add(Person(name="Margaret", surname="Hamilton", phone="01-234-567"))
directory.add(Business(name="Vedrai", phone="+39-333-333333"))
directory.add(Person(name="Linda", surname="Hamilton"))

assert len(directory) == 3

assert [el.phone for el in directory.query(name="Vedrai")] == ["+39-333-333333"]
assert [el.phone for el in directory.query(name="Margaret")] == ["01-234-567"]