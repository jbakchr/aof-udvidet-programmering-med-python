"""
Exercise 4

Based on your "Employer" and "Employee" classes do the following:

Add a "get_average_salary" method to the "Employer" class that returns the average salary.

Create an instance of your "Employer" class

Create 3 instances of your "Employee" class.

Add the 3 employee instances to the employer instance.

Call the "get_average_salary" method on your instance of the "Employer" class and print the result.
"""


class Employer:
    employees = []

    def __init__(self, name):
        self.name = name

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_average_salary(self):
        avg = 0
        for emp in self.employees:
            avg += emp.get_salary()
        return avg / len(self.employees)


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_salary(self):
        return self.salary


db = Employer("Danske Bank")

guido = Employee("Guido", 57, 100000)
niels = Employee("Guido", 45, 90000)
jonas = Employee("Guido", 41, 50000)

db.add_employee(guido)
db.add_employee(niels)
db.add_employee(jonas)

print(db.get_average_salary())
