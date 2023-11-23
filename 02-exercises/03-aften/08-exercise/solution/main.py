"""
Exercise 8

Import Pythons own "random" module.

Use the modules "randint" method to create a random integer between 1 and 6.
Save the random number in a variable called "num".

Use a while loop to keep creating a new random integer if "num" isn't six. 
"""
import random

num = random.randint(1, 6)

while num != 6:
    num = random.randint(1, 6)
    if num != 6:
        print(f"Damn .. you drew a {num}")

print("Hey!! You got the number 6!")
