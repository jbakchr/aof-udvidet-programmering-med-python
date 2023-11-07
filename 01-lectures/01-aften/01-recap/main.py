"""This file Python code / script is totally awesome"""

# variable
skip_num = 3

# datastructure - here a list
awesome_folks = ["Anika", "Hassan", "Kent", "Jonas", "Mette", "Niels"]


# function
def say_hello(index):
    print(f"Hi {awesome_folks[index]}")


# loop
for i in range(0, len(awesome_folks)):
    if i == skip_num:
        continue
    else:
        say_hello(i)
