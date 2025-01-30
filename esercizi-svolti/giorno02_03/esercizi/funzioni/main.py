# Scrivere il codice dell'esercizi qui dentro

#Esercizio 2 - parte 1

#implementazione funzione mydivmod()

def mydivmod(dividendo: int|float, divisore: int|float) -> tuple[int, int] | tuple[float, float]:
    """
        Calcola il quoziente ed il resto di una divisione rispettando l'equivalenza
        dividendo = quoziente * divisore + resto.

        Args:
            dividendo: int|float
            divisore: int|float

        Returns:
            tuple[int, int]: Se dividendo e divisore sono interi.
            tuple[float, float]: se il dividendo o il divisore è un float

        Raises:
            TypeError | ZeroDivisionError

        Example:
            >>> mydivmod( 4, 2)
            (2, 0)

            >>> mydivmod( 5, 2)
            (2, 1)
        """
    if not isinstance(dividendo, (int, float)) or not isinstance(divisore, (int, float)):
        raise TypeError("tipo errato")
    if divisore == 0:
        raise ZeroDivisionError("divisione per zero")

    return dividendo // divisore, dividendo % divisore


assert mydivmod(6, 4) == (1, 2)


# try:
#     print(mydivmod(5, 0))
# except TypeError as e:
#     print(f"{e}")
# except ZeroDivisionError as e:
#     print(f"{e}")







#Esercizio 2 - parte 2

def pow_list(seq: list[int | float]) -> list:
    """
        Mappa ogni elemento della sequenza fornita con l'elevamento al quadrato
        Args:
            seq: list[int|float]
        Returns:
            list: Ogni elemento sarà il quadrato di quello fornito
        Raises:
            Vuene sollevata l'eccezione TypeError per parametri non validi

        Example:
            >>> pow_list([1,2,3])
            [1,4,9]

    """
    result = []
    for el in seq:
        if isinstance(el, (int, float)):
            result.append(el**2)
        else:
            raise TypeError("la lista contiene dati non numerici")
    return result


# try:
#     pow_list([1.2,2,"a"])
# except Exception as e:
#     print(f"Error: {e.__class__} - {e}")

assert pow_list([1,2,3]) == [1,4,9]


def count_words(text: str) -> int:
    """
        Conta le parole in una stringa
        Args:
            text: str
        Returns:
            int: numero delle parole
        Raises:
            Vuene sollevata l'eccezione Typeerror per parametri non validi

        Example:
            >>> count_words("Mi chiamo Alessandro")
            3
    """
    if not isinstance(text, str):
        raise TypeError("Parametro non valido")

    return len(text.split())

# try:
#     print(count_words([1,2,3]))
# except Exception as e:
#     print(f"Error: {e.__class__} - {e}")

assert count_words("hello world")==2


def reverse_string(text: str) -> str:

    """
        Inverte le lettere di una stringa
        Args:
            text: str
        Returns:
            str: stringa invertita
        Raises:
            Vuene sollevata l'eccezione Typeerror per parametri non validi

        >>> reverse_string("Hello")
        'olleH'

    Note:
        Vengono illustrate più implementazioni:
        1. La stringa viene convertita in una lista per sfruttare il metodo `reverse`.
           Dopo aver modificato la lista sul posto, la stringa viene ricostruita usando `join`.
        2. Utilizzando la funzione reverced che accetta un iterabile e restituisce un iteratore
        3. Utilizzo dell'operatore [::-1] - slicing.
        4. Utilizzando un ciclo con un contatore decremento
    """
    if not isinstance(text, str):
        raise TypeError("Il parametro fornito non è una stringa.")

    creationist = list(text)
    creationist.reverse()
    return "".join(creationist)

def reverse_string2(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Il parametro fornito non è una stringa.")

    return "".join(reversed(text))

def reverse_string3(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Il parametro fornito non è una stringa.")

    return text[::-1]

def reverse_string4(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Il parametro fornito non è una stringa.")

    count=len(text)-1
    listainvertita=[]
    while count>=0:
        listainvertita.append(text[count])
        count-=1
    return "".join(listainvertita)

assert reverse_string("hello") == "olleh"


def reverse_string5(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Il parametro fornito non è una stringa.")

    count=len(text)-1
    while count>=0:
        yield text[count]
        count-=1

#print("".join(reverse_string5("alex")))





def is_palindrome(text: str) -> bool:
    """
        Verifica se la parola è un palindromo

        Args:
            text: str
        Returns:
            bool: True se la parola é un palindromo
        Raises:
            Vuene sollevata l'eccezione Typeerror per parametri non validi

        >>> is_palindrome("racecar")
        True
        """
    if not isinstance(text, str):
        raise TypeError("Il parametro fornito non è una stringa.")

    return text == text[::-1]


assert is_palindrome("racecar") == True




def sum_even_numbers(numlist: list[int|float]) -> int:
    """
        Somma i numeri nelle posizioni pari

        Args:
            numlist: int|float
        Returns:
            int: somma i valori nelle posizioni pari
        Raises:
            Vuene sollevata l'eccezione Typeerror per parametri non validi

        >>> sum_even_numbers([1, 2, 3, 4, 5])
        6


            """

    # result=0
    # for index, value in enumerate(numlist):
    #     if not isinstance(value, (int, float)):
    #         raise TypeError("La lista non contiene solo numeri")
    #
    #     if index%2:
    #         result +=value
    #
    # return result
    return sum(value for index, value in enumerate(numlist) if index%2)

assert sum_even_numbers([1, 2, 3, 4, 5]) == 6




def find_max(numlist: list[int|float]) -> int|float:
    """
        Trova il numero maggiore presente nella lista

        Args:
            numlist: int|float
        Returns:
            int|float: numero maggiore
        Raises:
            Vuene sollevata l'eccezione Typeerror per parametri non validi

        >>> find_max([3, 1, 4, 1, 5])
        5
    """
    for value in numlist:
        if not isinstance(value, (int, float)):
            raise TypeError("La lista non contiene solo numeri.")

    numlist.sort()
    return numlist[-1]


assert find_max([3, 1, 4, 1, 5]) == 5



def count_vowels(text: str) -> int:
    """
        Conta il numero di vocali nella stringa

        Args:
            text: stringa da esaminare
        Returns:
            int: numero di vocali trovate
        Raises:
            Vuene sollevata l'eccezione Typeerror per parametri non validi

        >>> count_vowels("hello world")
        3
    """
    if not isinstance(text, str):
        raise TypeError("Il parametro fornito non è una stringa.")

    vocal=["a", "e", "i", "o", "u"]
    count = 0
    for letter in text:
        if letter in vocal:
            count +=1
    return count



assert count_vowels("hello world") == 3



def factorial(num: int) -> int:
    """
        Calcola il fattoriale di un numero

        Args:
            num:
        Returns:
            int: fattoriale
        Raises:
            Vuene sollevata l'eccezione Typeerror per parametri non validi

        >>> factorial(5)
        120
    """
    if not isinstance(num, int):
        raise TypeError("Il parametro fornito non è un numero valido.")

    if num < 0:
        raise ValueError("Valori negativi non consentiti")

    if num > 1:
        return num * factorial(num -1)
    elif num == 1 or num ==0:
        return 1


# try:
#     print(factorial(-4))
# except Exception as e:
#     print(e)

assert factorial(5) == 120
