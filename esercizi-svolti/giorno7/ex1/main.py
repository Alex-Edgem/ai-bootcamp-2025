import random

def continua():

    nuovapartia = input("Vuoi continuare a giocare? si/no ")
    if nuovapartia.lower() == "si":
        return True
    return False



def indovina_il_numero():
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
                print(f"Hai indovinato il numero {numero_da_indovinare} in {tentativi} tentativi.")
                break

            if tentativi >= 3:
                print("Numero di tentativi a disposizione finiti")
                break

        continua_gioco = continua()

        if not continua_gioco:
            print("Arrivederci!!!")

indovina_il_numero()