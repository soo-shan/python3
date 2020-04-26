from collections.abc import Container
print("Container.__abstractmethods__ : ", Container.__abstractmethods__)
print()
help(Container.__contains__)

class OddContainer:
    """
    Duck type instance of Container class
    """

    def __contains__(self, x):
        """
        Return True if a given value is in the set of odd integers
        """
        # if not isinstance(x, int) or not x % 2:
        if not (isinstance(x, int) and (x % 2)):
            return False
        return True


odd_container = OddContainer()
print("isinstance(odd_container, Container): ",isinstance(odd_container, Container))
print("issubclass(OddContainer, Container): ", issubclass(OddContainer, Container))
# Any class that has a __contains__ method is a Container and can be queried by the in keyword
print("1 in odd_container", 1 in odd_container)
print("2 in odd_container", 2 in odd_container)
print("3 in odd_container", 3 in odd_container)
print('"string" in odd_container', "string" in odd_container)

