#Passing function as argument

def add(n:int):
    return  n + 10;

def mul(n:int):
    return n * 5;

def calculation(fn,val):
    print(fn(val));

print(calculation(add,20));

print(calculation(mul,5));


#Decorators

