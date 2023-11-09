"""
SOLUTION TO EXERCISE 2

Create a "Car" class with an init method that sets these arguments:
  - 1) "make" as a string
  - 2) "speed" as an integer
  - 3) "auto_gear" as a boolean
"""


class Car:
    def __init__(self, make, speed, auto_gear):
        self.make = make
        self.speed = speed
        self.auto_gear = auto_gear


volvo = Car("Volvo", 200, False)
tesla = Car("Tesla", 300, True)
