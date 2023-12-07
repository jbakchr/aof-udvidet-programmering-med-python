"""
Example 6 - reading separate lines from file
"""

f = open(
    "/Users/jonasphillipson/MyDocuments/AOF/udvidet-programmering-med-python/01-lectures/04-aften/06-read-lines-of-file/sometext.txt",
    "r",
)

# read first line
print(f.readline())

# read next (second) line
print(f.readline())

# read remaining lines by use of a loop
for text in f:
    print(text)
