"""
Examples of classes with and without the "str" method
"""


# Class without the "str" method
class Car:
    def __init__(self, make, speed):
        self.make = make
        self.speed = speed


# Class with the "str" method
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"


volvo = Car("Volvo", 200)
print(volvo)

lassie = Dog("Lassie", 7)
print(lassie)
