datatypes = [1, 1.5, "Jonas", True, ["apples", "beer"], {"name": "Jonas"}]


for el in datatypes:
    print(f"{el} is of type: {type(el)}")


def func():
    pass


print(type(func))
