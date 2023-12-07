"""
Exercise 6

Create a variable and assign it some text of your liking.

Open a file and write your text variable to that file.
"""

txt = "Learning Python is awesome!\nAnd oh .. we love you Guido <3"

file = open("./my_txt", "w")

file.write(txt)

file.close()
