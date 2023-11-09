"""
Example of the "init" method
"""


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


lassie = Dog("Lasse", 7)
print(f"Hi, my name is {lassie.name}")

lajka = Dog("Lajka", 5)
print(f"I'm {lajka.name} and I'm only {lajka.age} years old ..")
