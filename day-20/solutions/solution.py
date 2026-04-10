# Day 20 - OOP Inheritance & Dunder Methods | SOLUTION
# Try to solve exercises.py yourself before looking here!

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError
    def __str__(self):
        return f'{self.__class__.__name__}({self.name})'
class Dog(Animal):
    def speak(self):
        return 'Woof!'
class Cat(Animal):
    def speak(self):
        return 'Meow!'
for animal in [Dog('Rex'), Cat('Luna')]:
    print(animal, '->', animal.speak())
