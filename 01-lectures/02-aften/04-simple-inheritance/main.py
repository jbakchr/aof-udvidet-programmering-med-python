"""
Example of simple inheritance
"""


class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print("Wrooom!")


class Car(Vehicle):
    pass


c = Car("Volvo", 200)
c.drive()
