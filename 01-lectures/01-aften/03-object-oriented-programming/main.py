"""
Procedural vs Object Oriented Programming
"""

# PROCEDURAL PROGRAMMING

# Person 1
p1_name = "John Doe"
p1_job = "Programmer"
p1_salary = 50000

# Person 2
p2_name = "Guido van Rossum"
p2_job = "Programming GOD"
p2_salary = 50000000000


def give_a_raise(name, job):
    print(f"Should we give {name} a raise? ", end="")
    if job == "Programming GOD":
        print("Hell yeah!")
    else:
        print("Nope ..", end="\n\n")


def say_hello(name, job, salary):
    print(f"{name} is a {job} and makes {salary} a month")
    give_a_raise(name, job)


say_hello(p1_name, p1_job, p1_salary)
say_hello(p2_name, p2_job, p2_salary)
