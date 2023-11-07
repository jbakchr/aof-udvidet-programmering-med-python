# This file Python code / script is totally awesome
skip_num = 3

awesome_folks = ["Anika", "Hassan", "Kent", "Jonas", "Mette", "Niels"]


def say_hello(index):
    print(f"Hi {awesome_folks[index]}")


for i in range(0, len(awesome_folks)):
    if i == skip_num:
        continue
    else:
        say_hello(i)
