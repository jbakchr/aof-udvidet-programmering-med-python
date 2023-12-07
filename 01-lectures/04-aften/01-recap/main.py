"""
Recap from 3rd night
"""


# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"My name is {self.name} and roar like 'Wrrooaahhh!'")


# Child classes
class Tiger(Animal):
    def __init__(self, name, legs):
        super().__init__(name)  # super call
        self.legs = legs


class Snake(Animal):
    def speak(self):  # Method overriding
        print(f"My name is {self.name} and I .. don't roar")


# Polymorphism
for animal in [Tiger("Bob", 4), Snake("Mogens")]:
    animal.speak()
