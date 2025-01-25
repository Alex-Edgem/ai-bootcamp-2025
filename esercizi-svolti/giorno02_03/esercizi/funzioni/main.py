# Scrivere il codice dell'esercizi qui dentro
#Esercizio 2 - parte 1
from idlelib.configdialog import is_int
from operator import truediv


#implementazione funzione mydivmod()
#in caso di valori non validi o dividendo 0 restituisce None che viene gestito sulla chiamata
def mydivmod(dividendo,divisore):
    """
    Restituisce il quoziente e il resto della divisione (a // b, a % b).

    Args:
        a (int | float): Il dividendo.
        b (int | float): Il divisore.

    Returns:
        tuple: Una tupla (quoziente, resto) o None in caso di errore."""
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
    """
    Restituisce il quoziente e il resto della divisione (a // b, a % b).

    Args:
        a (int | float): Il dividendo.
        b (int | float): Il divisore.

    Returns:
        tuple: Una tupla (quoziente, resto)."""
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
    """
    Restituisce il quoziente e il resto della divisione (a // b, a % b).

    Args:
        a (int | float): Il dividendo.
        b (int | float): Il divisore.

    Returns:
        tuple: Una tupla (quoziente, resto)"""
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
    """mydivmod2(a: int|float, b: int|float) -> tuple

        Restituisce il quoziente e il resto della divisione (a // b, a % b).

        Args:
            a (int | float): Il dividendo.
            b (int | float): Il divisore.

        Returns:
            tuple: Una tupla (quoziente, resto)"""
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
    """
    Args:
        numbers (list): Lista di numeri (int o float).

    Returns:
        list: Nuova lista con ogni elemento elevato alla potenza di 2.
    """
    result =[]
    for el in seq:
        result.append(el**2)
    return result





def count_words(string):
    return len(string.split(" "))




def reverse_string(text):
    creationist=list(text)
    creationist.reverse()
    return "".join(creationist)

def reverse_string2(text):
    return "".join(reversed(text))

def reverse_string3(text):
    return text[::-1]

def reverse_string4(text):
    count=len(text)-1
    list=[]
    while count>=0:
        list.append(text[count])
        count-=1
    return "".join(list)





def is_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False



def sum_even_numbers(li):
    result=0
    for num in li:
        result +=num
    return result


def find_max(li):
    li.sort()
    return li[-1]




def count_vowels(st):
    vocal=["a", "e", "i", "o", "u"]
    vocalinstring=[]
    for letter in st:
        if letter in vocal:
            vocalinstring.append(letter)
    return len(vocalinstring)



