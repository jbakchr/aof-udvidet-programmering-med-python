"""
Examples of local and global scope
"""

# Global scope
num = 10


def func():
    # Local scope - assignment does not change "global" scope
    num = 5
    print(f"Local scope: {num}")


func()

print(f"Global scope: {num}")
