import random
import csv
import datetime

def continua():
    nuovapartia = input("Vuoi continuare a giocare? si/no ")
    if nuovapartia.lower() in "si":
        return True
    return False

def caricadati():
    with open("score.csv") as fd:
        reader = csv.reader(fd)
        head = next(reader)
        data = sorted(reader, key = lambda x: int(x[1]))
        return head, data


def scrividati(head, data):
    with open("score.csv", "w", newline='') as fd:
        writer = csv.writer(fd)
        writer.writerow(head)
        writer.writerows(data)


def indovina_il_numero():
    head, data = caricadati()
    bestscore = int(data[0][1])
    inizio_partita = datetime.datetime.now()
    fine_partita = None
    continua_gioco = True
    while continua_gioco:
        numero_da_indovinare = random.randint(1, 100)
        tentativi = 0

        print("Benvenuto nel gioco 'Indovina il numero' tra 1 e 100")

        while True:
            try:
                numero_utente = int(input("Inserisci il tuo numero: "))
            except ValueError:
                print("Inserisci un numero valido.")
                continue

            tentativi += 1

            if numero_utente < numero_da_indovinare:
                print("Troppo basso! Riprova.")
            elif numero_utente > numero_da_indovinare:
                print("Troppo alto! Riprova.")
            else:
                fine_partita = datetime.datetime.now()
                durata_in_secondi = int((fine_partita - inizio_partita).total_seconds())
                print(f"Hai indovinato il numero {numero_da_indovinare} in {tentativi} tentativi.")
                if tentativi < bestscore:
                    nome_utente = input("Nuovo Record !!!!! Inserisci il tuo nome! ")
                    data.insert(0,[nome_utente, tentativi, datetime.datetime.now().strftime('%Y-%m-%d %H:%M'), durata_in_secondi])
                    scrividati(head, data)
                break

            if tentativi >= 99:
                print("Numero di tentativi a disposizione finiti")
                break

        continua_gioco = continua()

        if not continua_gioco:
            print("Arrivederci!!!")

indovina_il_numero()