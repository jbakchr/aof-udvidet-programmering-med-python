"""
Exercise 3

Firstly, create these 2 classes:
- An "Employer" class
- An "Employee" class

The "Employer" class should:
- have a class attribute called "employees" set to an empty list
- have its "init" take a "name" argument
- have one method that adds an "employee" to its list of employees

The "Employee" class should:
- have an "init" method with a "name", "age" and "salary" argument
- have a method called "get_salary" that returns the employee salary
"""


class Employer:
    employees = []

    def __init__(self, name):
        self.name = name

    def add_employee(self, employee):
        self.employees.append(employee)


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_salary(self):
        return self.salary
