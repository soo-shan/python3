class EvenOnly(list):
    """
    This class creates a list which allows only even numbers as input
    """
    def append(self, integer):
        """
        Append an even integer to the list
        """
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)


even_list = EvenOnly([12,14])
even_list.append(10)
print(even_list)
even_list.append(5)
even_list.append(12.0)
