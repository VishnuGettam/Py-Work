Step 1: Python starts reading the file

Python executes from top to bottom.

from typing import Any

Imports Any.

Then Python sees

class decorator_class:

At this point,

Python does not execute __init__() or __call__().

It simply creates a class object in memory.

Memory now looks like

Memory
│
├── decorator_class (class object)
│      │
│      ├── __init__()
│      └── __call__()

Nothing else happens.

Step 2: Python reaches
@decorator_class
def sum(a,b,c):
    ...

This is where most beginners get confused.

Python does NOT immediately create sum as a normal function.

Instead it internally converts this into

def sum(a,b,c):
    print(...)

sum = decorator_class(sum)

Python literally behaves as if you wrote the above code.

Step 3: Function creation

First Python creates the function object.

Memory

sum  ------> Function Object

Now

sum

points to the original function.

Step 4: Decorator executes

Now Python executes

decorator_class(sum)

Since this is creating an object,

Python calls

__init__()

internally.

Equivalent to

obj = decorator_class(sum)

Python automatically does

obj.__init__(sum)

Inside

def __init__(self, original_function):

this happens

self.original_function = original_function

Now the object contains

decorator_class object
│
└── original_function
        │
        ▼
      sum()
Step 5: Replace function

After object creation,

Python assigns

sum = obj

Notice something important.

Originally

sum
   │
   ▼
Function

Now

sum
   │
   ▼
decorator_class object

The original function is no longer directly referenced by sum.

Instead

sum
   │
   ▼
decorator_class object
        │
        ▼
original_function
        │
        ▼
Function

This is the key idea of decorators.

Memory after decoration
sum
 │
 ▼
decorator_class object
 │
 └──────────────┐
                │
original_function
                │
                ▼
          sum function
Step 6: Python reaches
if __name__ == "__main__":

Condition is True.

Now Python executes

sum(4,7,9)

But...

Is sum a function anymore?

No.

It is now an object.

sum
 │
 ▼
decorator_class object
Step 7: Why doesn't Python throw an error?

Because your class defines

__call__()

Objects having

__call__()

can be called like functions.

Python internally converts

sum(4,7,9)

into

sum.__call__(4,7,9)

where sum is actually the object.

Step 8: Enter call()

Now execution enters

def __call__(self,*args,**kwargs):

Here

self

is the decorator object.

args

contains

(4,7,9)

So

self.original_function

points to the original function.

decorator object
│
└── original_function
          │
          ▼
      original sum()
Step 9: Print function name
print(self.original_function.__name__)

prints

function name - sum

because

self.original_function

is the original function object.

Step 10: Execute original function

Now

return self.original_function(*args, **kwargs)

becomes

return original_sum(4,7,9)

Tuple unpacking happens:

args

(4,7,9)

↓

a = 4
b = 7
c = 9

The original function executes

sum of 4 && 7 && 9 - 20
Complete Execution Flow
Program Starts
      │
      ▼
Import Any
      │
      ▼
Create decorator_class
      │
      ▼
Create function object (sum)
      │
      ▼
Decorator executes
decorator_class(sum)
      │
      ▼
Calls __init__()
      │
      ▼
Stores original function
      │
      ▼
Returns decorator object
      │
      ▼
sum now refers to decorator object
      │
      ▼
Reach if __name__ == "__main__"
      │
      ▼
sum(4,7,9)
      │
      ▼
Actually calls
sum.__call__(4,7,9)
      │
      ▼
Print function name
      │
      ▼
Call original function
      │
      ▼
Original function executes
      │
      ▼
Program Ends
Visual Memory Diagram
                sum variable
                     │
                     ▼
         +-------------------------+
         | decorator_class object  |
         +-------------------------+
         | original_function ------|------------------+
         +-------------------------+                  |
                                                      |
                                                      ▼
                                         +----------------------+
                                         | Original sum()       |
                                         +----------------------+
                                         | a,b,c parameters     |
                                         +----------------------+
Why use a class instead of a function decorator?

A function decorator:

def decorator(func):
    def wrapper(*args, **kwargs):
        ...
        return func(*args, **kwargs)
    return wrapper

stores the original function inside a closure (wrapper).

A class decorator:

class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        ...
        return self.func(*args, **kwargs)

stores the original function as an instance attribute (self.func).

Both achieve the same result, but class decorators make it easier to maintain state across calls (for example, counting how many times a function has been invoked). Since you're learning decorators, it's valuable to understand both approaches because they illustrate two different but equally common Python techniques.