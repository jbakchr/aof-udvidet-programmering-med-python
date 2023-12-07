"""
Exercise 1

In this exercise you are to create a parent "Shape" class and two child classes called
"Square" and "Triangle" that'll inherit from the "Shape" class.

First create the Shape class with a constructor function taking a "width" and a "height"
argument.

Add a "calculate_area" method to the "Shape" class and make it return the multiplication
of its two attributes.

Next create a "Square" class that inherits from the "Shape" class but doesn't do anything
else than that.

Then create a "Triangle" class that also inherits from the "Shape" class but which overrides
the "calculate_area" method by use of calling its super method and dividing the result by 2.

Finally, create a list containing both a "Square" and a "Triangle" instance. Loop through this
list and call the "calculate_area" method by use of polymorphism.
"""
