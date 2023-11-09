"""
Exercise 6

Add the following methods to your "Dog" class from exercise 5:
- 1) an "__init__" method with a name and age argument
- 2) a "get_name" method that returns the name of the dog
- 3) a "get_age" method that returns the age of the dog
- 4) a "set_name" method that changes the name of the dog
- 5) a "set_age" method that changes the age of the dog

Create an instance of your Dog class and use your 'get' and 'set' methods.
"""


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age


d = Dog("Lassie", 89)

d.set_name("Lajka")
print(d.get_name())

d.set_age(9000)
print(d.get_age())
