"""
Example of how to add a variable to global scope from within a function
"""


# Add global variable
def add_global_var():
    global num
    num = 10


add_global_var()
print(num)  # prints 10


# Change global var
def change_global_var():
    global num
    num = 20


change_global_var()
print(num)  # prints 20
