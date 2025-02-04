import json

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
                    hasattr(contact, "surname") and param in contact.surname or
                    (contact.phone and param in contact.phone)]

    def save(self, path):
        with open(path, 'w') as file:
            json.dump([contact.__dict__ for contact in self.rubrica], file)

    def load(self, path):
        with open(path, 'r') as file:
            data = json.load(file)
            self.rubrica = [Person(**contact) if 'surname' in contact else Business(**contact) for contact in data]

class Person:
    def __init__(self, name, surname, phone=None):
        self.name = name
        self.surname = surname
        self.phone = phone

class Business:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Interfaccia:
    def __init__(self):
        self.directory = Directory()
        self.commands = {
            'a': ("Add", self.add_contatto),
            'f': ("Find", self.find_contatto),
            's': ("Save (JSON)", self.save_contatti),
            'l': ("Load (JSON)", self.load_contatti),
            'h': ("Menu", self.mostra_comandi),
            'q': ("Exit", self.exit_program),
        }

    def mostra_comandi(self):
        main_menu = [
            ("a (person|business)", "Add"),
            ("f <text>", "Find"),
            ("s <path>", "Save (JSON)"),
            ("l <path>", "Load (JSON)"),
            ("q", "Exit"),
            ("h", "Menu"),
            ("Invio", "Continua")
        ]

        print("\033[1;37;40m" + "Commands:".ljust(41) + "\033[0m")
        for command in main_menu:
            print(command[0].ljust(30) + command[1])
        print("\n")

    def menu(self):
        while True:
            self.mostra_comandi()
            comando = input("Inserisci un comando: ").lower()

            if comando in self.commands:
                # Esegui il comando associato
                self.commands[comando][1]()
            else:
                print("Comando non valido.")

    def add_contatto(self):
        tipo = input("Aggiungi (p)ersona o (b)usiness? ").lower()
        if tipo == 'p':
            name = input("Nome: ")
            surname = input("Cognome: ")
            phone = input("Telefono: ")
            person = Person(name, surname, phone)
            self.directory.add(person)
        elif tipo == 'b':
            name = input("Nome business: ")
            phone = input("Telefono: ")
            business = Business(name, phone)
            self.directory.add(business)

    def find_contatto(self):
        param = input("Inserisci il parametro di ricerca: ")
        result = self.directory.find(param)
        if result:
            for contact in result:
                print(f"{contact.name}, {getattr(contact, 'surname', '')}, {contact.phone}")
        else:
            print("Nessun contatto trovato.")

    def save_contatti(self):
        path = input("Inserisci il percorso del file per salvare: ")
        self.directory.save(path)
        print(f"Contatti salvati in {path}.")

    def load_contatti(self):
        path = input("Inserisci il percorso del file per caricare: ")
        self.directory.load(path)
        print(f"Contatti caricati da {path}.")

    def exit_program(self):
        print("Uscita dal programma.")
        exit()

rubric = Interfaccia().menu()