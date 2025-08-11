# Encapsulation
class EncapsulationExample:
    def __init__(self, a, b):
        self._a = a
        self.__b = b  # private attribute

    def sum(self):
        return self._a + self.__b

encap = EncapsulationExample(10, 20)
print("Encapsulation Example: ", encap.sum())
