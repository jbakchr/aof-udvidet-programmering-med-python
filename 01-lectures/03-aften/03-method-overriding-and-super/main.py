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
    def __init__(self, brand, speed, wheels):
        super().__init__(brand, speed)
        self.wheels = wheels

    def drive(self):
        print("My car is driving")


class Bus(Vehicle):
    def __init__(self, brand, speed, wheels):
        super().__init__(brand, speed)
        self.wheels = wheels


c = Car("Audi", 300, 4)
c.drive()  # prints "My car is driving"

b = Bus("Volvo", 200, 12)
b.drive()  # print "Wrooom!"
