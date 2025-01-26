def pow_list(seq: list[int]) -> list[int]:
    """
        Mappa ogni elemento della sequenza fornita con l'elevamento al quadrato


        Args:
            seq: list[int]


        Returns:
            list[int2]: Ogni elemento sarà il quadrato di quello fornito

        Raises:
            Non viene sollevato nessun errore. Si deve estire il valore di ritorno None.

        Example:
            >>> pow_list([1,2,3])
            [1,4,9]

        """
    result = []
    for el in seq:
        result.append(el ** 2)
    return result

print(pow_list([1,2,3]))