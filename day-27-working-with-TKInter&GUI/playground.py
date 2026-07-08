"""
*args means it can many positional arguments

we can also print out the number at an index as it will act as tuple
ex - args[0] will be 2 and args[1] will be 3
"""

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(2,3,4,5,6,7,8,9))

"""
**kwargs means it can many keyword arguments

here it will act as dict
"""

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)

calculate(2, add=3, multiply=3)
