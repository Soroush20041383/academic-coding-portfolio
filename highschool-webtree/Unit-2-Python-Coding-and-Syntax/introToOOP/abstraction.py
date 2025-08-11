# Abstraction
from abc import ABC, abstractmethod

class AbstractClassExample(ABC):
    @abstractmethod
    def do_something(self):
        pass

class AnotherSubclass(AbstractClassExample):
    def do_something(self):
        super().do_something()
        print("The subclass is doing something")

x = AnotherSubclass()
x.do_something()
