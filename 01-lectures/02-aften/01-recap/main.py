"""
Example 1 - Recap
"""


class Car:
    wheels = 4

    def __init__(self, brand, speed, wheels):
        self.brand = brand
        self.speed = speed

        if wheels != 4:
            self.wheels = wheels

    def __str__(self):
        return f"Brand: {self.brand}, Speed: {self.speed}, Wheels: {self.wheels}"


c1 = Car("Skoda", 200, 4)
print(c1)

c2 = Car("Audi", 300, 3)
print(c2)
