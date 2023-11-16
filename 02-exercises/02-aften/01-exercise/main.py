"""
Exercise 1

Create a Dog class that has the following:
- A class attribute variable called "legs" that is set to 4
- An "__init__" method that takes "name", "age" and "legs" as arguments
  - The init method check if the "legs" argument is not 4 and if so change the class attribute
- A "__str__" method that returns a string represention of your class attributes anyway you like

Create two instances of your Dog class. One have 4 legs. The other only 3.
"""


class Dog:
    legs = 4

    def __init__(self, name, age, legs):
        self.name = name
        self.age = age

        if legs != 4:
            self.legs = legs

    def __str__(self):
        return f"Hi, my name is {self.name}, I'm {self.age} years old, and have {self.legs} legs"


d1 = Dog("Jonas", 99, 17)
print(d1)

d2 = Dog("Django", 3, 4)
print(d2)
