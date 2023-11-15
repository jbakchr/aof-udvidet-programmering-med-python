"""
Exercise 3

Based on your car class from the previous exercise do the following:

First, add a method called "gear_up" that increments the "gear" attribute by 1 (but only if the gear is not already at a max of 6).
If the method increments the gear then print which gear the car is now in.


Lastly, add a method called "gear_down" that decreases the "gear" attribute by 1 (but only if the gear does not go below 0).
If the method decreases the gear then print which gear the car is now in.

Create an instance of your car class and play around calling your two new methods on it.
"""


class Car:
    gear = 0

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def start(self):
        print("Wrooom!")

    def gear_up(self):
        if self.gear != 6:
            self.gear += 1
            print(f"Your {self.brand} is now in gear {self.gear}")

    def gear_down(self):
        if self.gear != 0:
            self.gear -= 1
            print(f"Your {self.brand} is now in gear {self.gear}")


c = Car("Audi", 300)
c.gear_up()
c.gear_down()
