"""
Exercise 3

Based on your classes from exercise 2 please do the following:

Add the "init" method to the "Student" and make it take an additional "grade" argument.

Override the "hello" method in the "Student" class and print something other than its parent.

"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def hello(self):
        print(self.name, self.age, self.grade)


s = Student("Jonas", 41, 100)
s.hello()
