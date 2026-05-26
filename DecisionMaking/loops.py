"""
    For -> sequence based
    While  -> condition based
"""

_agelist = [5,14,17,20,46]


print("---------skip---------")
for x in _agelist:   

# skip the iteration and moves to next 
    if x == 17:
        continue

    print(f" Age : {x} ")

print("---------break---------")
for x in _agelist:   

# skip the iteration and moves to next 
    if x == 17:
        break

    print(f" Age : {x} ") 

print("---------While---------")

num_iterations = 1
while(num_iterations <= 10):
    print(f"Iteration count : {num_iterations} ")

    num_iterations+= 1

