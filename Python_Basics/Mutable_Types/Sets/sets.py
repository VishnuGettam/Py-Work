
"""
    Sets - Unordered collection of unique items(No duplicates allowed) and can be any type
        carry out mathematical set operations like union, intersection,
        difference and symmetric difference
"""

#Creating a set
my_set = {1, 2, 3, 4, 5}
print("Initial set:", my_set)

data = {1, 2, 2, 3, 4, 4, 5}
print("Set with duplicates (duplicates removed):", data)

# heterogenous set
user_info ={1,2,"blr","ctr",(4,5,"hyd")}

print(f"Heterogenous set - {user_info}")


a = {1,2,3,4,5}
b={4,5,6,7,8}

# union 
c = a | b

print(f" Union of A | B : {c}  ")

# intersection
d = a & b

print(f" Intersection of A & B : {d} ")

# Diff of 2 sets (a set of elements that are only in A but not in B.)

e = a - b 

print(f" Set difference (a-b): {e} ")


# Diff of 2 sets (a set of elements that are only in B but not in A.)

f = b - a 

print(f" Set difference (b-a): {f} ")

# set symmetric difference

g = a ^ b

print(f"set symmetric diff : {g}")

# iteration in set
for _letter in set("apple"):
    print(_letter)