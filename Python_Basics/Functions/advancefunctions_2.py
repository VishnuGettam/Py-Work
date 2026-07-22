"""
    reduce : iterates through the sequence and produce a single result
    generator : yield keyword

    diff b/w yield vs return
"""


# reduce function importing from functools module
from functools import reduce

ip = [4,5,6,7]
op = reduce( lambda x,y : x + y ,ip)

print(f" reduce funtions op : {op} ")



# generator function 
# any function defined with yield keyword will become generator function

def simple_GenFunction():
    yield 1
    yield 2
    yield 3

# x is generator object
x = simple_GenFunction()


print(x.__next__());
print(x.__next__());
print(x.__next__());