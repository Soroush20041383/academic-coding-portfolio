# Polymorphism
class Cat:
    def sound(self):
        return 'Meow!'

class Dog:
    def sound(self):
        return 'Woof!'

def make_sound(animal):
    print(animal.sound())

cat_obj = Cat()
dog_obj = Dog()

make_sound(cat_obj)  # Outputs 'Meow!'
make_sound(dog_obj)  # Outputs 'Woof!'