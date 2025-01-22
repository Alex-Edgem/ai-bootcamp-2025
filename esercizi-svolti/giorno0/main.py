#funzione print()
print("ciao, mondo!")
print(40+2)

#Commentato perche restituisce eccezione
#print(40/0)

#stampa a video
testoDelFile=None
with open("README.md", "r") as file:
        testoDelFile = file.read()
        print(testoDelFile)

#stampa su file
with open("stampaSuFile.txt","w") as file:
        print("ciao, mondo!", file=file)

