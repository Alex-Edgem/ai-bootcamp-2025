import csv
import sqlite3

class Datafile:
    def __init__(self, path):
        self.path = path
        self.file_data = []
        with open(self.path, encoding="utf-8", newline="") as file:
            reader = csv.reader(file, delimiter=";")
            self.file_data = [el for el in reader if el]

    def __iter__(self):
        return iter(self.file_data)


class Database:
    def __init__(self, db_path=None):
        self.conn = None
        self.db_path = db_path
        self.tables = []

    def create_db(self, db_path=None):
        if db_path and ".db" in db_path:
            self.conn = sqlite3.connect(db_path)
            print("Database creato")
        else:
            print("Indicare il nome del db")
            db_path = input(">>> ")
            if db_path and ".db" in db_path:
                self.conn = sqlite3.connect(db_path)
                print("Database creato")
            else:
                self.conn = sqlite3.connect(db_path + ".db")
                print("Database creato con estensione .db")

    def close_db(self):
        if self.conn:
            self.conn.close()


class Table:
    def __init__(self, db):
        self.db = db
        self.table_name = None

    def create_table(self, table_name=None):
        if table_name is None:
            table_name = input("Assegna un nome alla tabella: ")
            print(f"Nome assegnato alla tabella {table_name}")
        self.table_name = table_name

        cur = self.db.conn.cursor()
        query = f"""
                    CREATE TABLE IF NOT EXISTS {table_name} (
                        id INTEGER PRIMARY KEY,
                        first_name TEXT,
                        last_name TEXT,
                        year_of_birth DATE,
                        gender TEXT,
                        email TEXT,
                        assignments INTEGER
                    )
                """
        cur.execute(query)
        self.db.conn.commit()
        self.db.tables.append(table_name)

    def load_data(self, data_to_load=None):
        if data_to_load is None:
            print("Hai dimenticato di passare i dati da caricare nella tabella")
            return
        header = [column for column in data_to_load[0]]
        rows = [row for row in data_to_load[1:]]

        cur = self.db.conn.cursor()
        query = f"""
                INSERT INTO {self.table_name} ({', '.join(header)}) 
                VALUES ({', '.join(['?'] * len(header))}) 
                ON CONFLICT(id) DO NOTHING;
            """
        cur.executemany(query, rows)
        self.db.conn.commit()
        print(f"{len(rows)} righe inserite nella tabella '{self.table_name}'.")

    def students_by_year(self, year):
        cur = self.db.conn.cursor()
        query = f"""
            SELECT * FROM {self.table_name} WHERE year_of_birth = {year};
        """
        cur.execute(query)
        students = cur.fetchall()
        for student in students:
            print(student)

    def max_assignments(self):

        cur = self.db.conn.cursor()

        query = f"""
            SELECT first_name, last_name, MAX(assignments) FROM {self.table_name};
        """
        cur.execute(query)
        max_assignments = cur.fetchone()
        print(f"{max_assignments[0]} {max_assignments[1]} con {max_assignments[2]} assignments")

    def find_students_Jane(self):
        cur = self.db.conn.cursor()

        query = f"""
            SELECT last_name FROM {self.table_name} WHERE first_name = 'Jane';
        """
        cur.execute(query)
        surname_students = cur.fetchall()
        print("\nJane surname:")
        for surname in surname_students:
            print(surname[0])

    def sorted_by_assignments(self):
        cur = self.db.conn.cursor()

        query = f"""
            SELECT first_name, last_name, assignments FROM {self.table_name} ORDER BY assignments DESC;
        """
        cur.execute(query)
        students_sorted = cur.fetchall()

        print("\nGraduatoria degli studenti ordinati per numero di assignments:")
        for student in students_sorted:
            print(f"{student[0]} {student[1]}:".ljust(25) + f"{student[2]} assignments")



# Creazione dell'istanza di Datafile
data = Datafile("students.csv")  # Nome del file/percorso da implementare

# Creazione del database
db = Database()
db.create_db("students.db")

# Creazione della tabella
students = Table(db)
students.create_table("students")

# Caricamento dei dati nella tabella
students.load_data(data.file_data)  # Passa data.file_data, non data

# Test: Trova gli studenti nati nel 2000
print("Studenti nati nel 2000:")
students.students_by_year(2000)

# Test: Trova lo studente con il massimo numero di assignments
print("\nStudente con il massimo numero di assignments:")
students.max_assignments()

# Test: Trova i cognomi degli studenti chiamati 'Jane'
print("\nCognomi degli studenti chiamati Jane:")
students.find_students_Jane()

# Test: Ordina gli studenti per numero di assignments (decrescente)
students.sorted_by_assignments()

# Chiudi la connessione
db.close_db()
