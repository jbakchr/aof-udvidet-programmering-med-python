"""
Exercise 5

In this exercise you are read the provided txt file and print its content in
a certain way.

Hence, first open the "quotes.txt" file and save it to a variable.

Loop through your variable line by line and:
- strip the line of the new line escape character (i.e. "\n")
- split each line by a colon (i.e. ":")
- print a line where the indexes of the splitted line is reversed to your liking

Lastly, make sure to close your file.
"""

file = open("./quotes.txt", "r")

for quote in file:
    split_quote = quote.strip("\n").split(":")
    print(f"{split_quote[1]} - {split_quote[0]}")

file.close()
