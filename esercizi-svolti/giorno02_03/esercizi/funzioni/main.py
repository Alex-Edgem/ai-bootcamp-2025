# Scrivere il codice dell'esercizi qui dentro
#Esercizio 2 - parte 1
from idlelib.configdialog import is_int


#implementazione funzione mydivmod()
#in caso di valori non validi o dividendo 0 restituisce None che viene gestito sulla chiamata
def mydivmod(dividendo,divisore):
    """[a=int|float|str, b=int|float|str] -> (a//b,a%b)|None"""
    #q*d + r = a
    if not isinstance(dividendo,(int,float)) or not isinstance(divisore,(int,float)):
        return None
    if divisore == 0:
        return None

    return (dividendo//divisore,dividendo % divisore)

assert mydivmod(6,4) ==(1,2)
assert mydivmod(6,"a") is None
#Non posso usare isinstance con None perchè ?


# result=mydivmod(-7.5,"a")
# if result == None:
#     print("stai usando valori non validi 1")
# else:
#     print(result)



#in caso di valori non validi o dividenzo 0 vengono lanciati errori di tipo diverso
#La chiamata viene gestita con try e 2 excep (i due tipi di errore previsti)
#presuppone la conoscenza degli errori previsti


def mydivmod2(dividendo,divisore):
    """[a=int|float|str, b=int|float|str] -> (a//b,a%b)"""
    #q*d + r = a
    if not isinstance(dividendo,(int,float)) and not isinstance(divisore,(int,float)):
        raise TypeError("tipo errato")
    if divisore == 0:
        raise ZeroDivisionError("divisione per zero")

    return (dividendo//divisore,dividendo % divisore)

assert mydivmod2(6,4) ==(1,2)
#assert not isinstance(mydivmod2(6, 0), tuple) Errore perche non viene restituito ma sollevato
#assert mydivmod2(6,"a") is TypeError # Errore perche non viene restituito ma sollevato

# try:
#     print(mydivmod2(5, 0))
# except TypeError:
#     print("tipo errato")
# except ZeroDivisionError:
#     print("divisione per zero")



#in caso di valori non validi o dividenzo 0 vengono lanciati errori di tipo diverso
#non presuppone la conoscenza degli errori previsti - ho usato Exception

def mydivmod3(dividendo,divisore):
    """[a=int|float|str, b=int|float|str] -> (a//b,a%b)"""
    #q*d + r = a
    if not isinstance(dividendo,(int,float)) and not isinstance(divisore,(int,float)):
        raise TypeError("tipo errato")
    if divisore == 0:
        raise ZeroDivisionError("divisione per zero")

    return (dividendo//divisore,dividendo % divisore)

assert mydivmod3(6,4) ==(1,2)

# try:
#     print(mydivmod3(5, 0))
# except Exception as e:
#     print(e)


#try dentro definizione di funzione
def mydivmod4(dividendo,divisore):
    try:
        return (dividendo//divisore, dividendo%divisore)
    except Exception as error:
        if type(error)==TypeError:
            return "Tipi non validi"
        else:
            return "Stai tentando di dividere per Zero"


assert isinstance(mydivmod4(6,0),str)

# print(mydivmod4(5, ""))





#Esercizio 2 - parte 2

def pow_list(seq):
    result =[]
    for el in seq:
        result.append(el**2)
    return result

print(pow_list((2,3)))

