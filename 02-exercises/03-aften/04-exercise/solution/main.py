"""
Exercise 4

Create a parent "Animal" class with a "speak" method that print "Wrooaahh!"

Create a child "Tiger" class that only inherits from the "Animal" class.

Create another child class called "Cat" that inherits from the "Animal" class but overrides its "speak" method.

Call the "speak" in the provided loop.
"""


class Animal:
    def speak(self):
        print("Wrooaahh!")


class Tiger(Animal):
    pass


class Cat(Animal):
    def speak(self):
        print("Meoow!")


for animal in (Tiger(), Cat()):
    # call the "speak" method here
    animal.speak()
