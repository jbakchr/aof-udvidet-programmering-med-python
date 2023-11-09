"""
Exercise 3

Create a class called "Car that takes these arguments in the "init" method:
- 1) make
- 2) speed

Instantiate an object of the class and print it's string representation to the console.
"""


class Car:
    def __init__(self, make, speed):
        self.make = make
        self.speed = speed


volvo = Car("Volvo", 200)
print(volvo)
