"""
Exercise 2

Create a "Car" class that:
- has a class attribute called "gear" set to 0
- has an init method that takes a "brand" and "speed" argument
- has a class method called "start" that just print "Wrooom!"

Lastly, create an instance of your car class.
"""


class Car:
    gear = 0

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def start(self):
        print("Wrooom!")


c = Car("Audi", 300)
