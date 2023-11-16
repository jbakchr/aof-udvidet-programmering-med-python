class Car:
    def move(self):
        print("Drive!")


class Boat:
    def move(self):
        print("Sail!")


class Plane:
    def move(self):
        print("Fly!")


for element in (Car(), Boat(), Plane()):
    element.move()
