"""
Exercise 6

Create a "Person" class that act as the "Parent" class which will take these arguments:
- name
- age

Create a method called "hello" for the "Person" class that prints out the name and age attribute

Create a simple "Student" class that inherits from the "Person" class but that doesn't do anything.

Create an instance of your "Student" class and call the "hello" method
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print(self.name, self.age)


class Student(Person):
    pass


s = Student("Jonas", 41)
s.hello()
