"""
Exercise 5

Just create simple integer variable with the same name inside and outside of a function
and print value of these two variables to the console.

** Note from Jonas about the exercise **
This exercise is obviously very simple but the main thing is just for you get started
getting experience with scope as a concept.
"""

num = 10


def func():
    num = 5
    print(num)


func()

print(num)
