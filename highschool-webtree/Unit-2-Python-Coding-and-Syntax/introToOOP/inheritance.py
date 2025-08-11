# Inheritance
class Parent:
    def greet(self):
        print("Hello from parent!")

class Child(Parent):
    def greet(self):
        print("Hello from child!")

parent = Parent()
child = Child()

parent.greet()
child.greet()