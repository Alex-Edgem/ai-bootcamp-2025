def sum_even_numbers(numlist: list[int|float]) -> int:
    """
        Somma i numeri nelle posizioni pari

        Args:
            list: int|float
        Returns:
            int: somma i valori nelle posizioni pari
        Raises:
            Vuene sollevata l'eccezione Typeerror per parametri non validi

        >>> sum_even_numbers([1, 2, 3, 4, 5])
        6


            """

    result=0
    for index, value in enumerate(numlist):
        if not isinstance(value, (int, float)):
            raise TypeError("Il parametro fornito non è un numero.")

        if index%2:
            result +=value

    return result

print(sum_even_numbers([1, 2, 3, 4, 5]))