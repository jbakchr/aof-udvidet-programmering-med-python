"""
Exercise 4

Create a class called "Person" with the arguments in the "init" method:
- 1) name
- 2) age
- 3) job

Define the "__str__(self)" method for the class in any way you like.

Instantiate one object of the class and print it to the console.
"""


class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def __str__(self):
        return f"name: {self.name}, age: {self.age}, job: {self.job}"


guido = Person("Guido", 58, "programmer")
print(guido)
