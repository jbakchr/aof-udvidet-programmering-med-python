"""
Exercise 4

In this exercise you install and use an external Python package called
"requests" to fetch a list of fake posts in json format and from the response
save it to a ".json" file.

Hence, start by installing the "requests" package using "pip".

Next, import requests, create a variable called "url" below and set it equal to this string:
  - https://jsonplaceholder.typicode.com/posts/

Then create a variable called "response" and assign it the result of calling the "get" method
on your requests import.

Finally, run your script from the terminal leaving the supplied code at the bottom as is.
"""

# Start your code below here


# Code supplied by Jonas
with open("./posts.json", "w") as f:
    f.write(response.text)
