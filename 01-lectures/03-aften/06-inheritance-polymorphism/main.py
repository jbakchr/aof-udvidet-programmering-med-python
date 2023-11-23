class Vehicle:
    def move(self):
        print("Move ..")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


for element in (Car(), Boat(), Plane()):
    element.move()
