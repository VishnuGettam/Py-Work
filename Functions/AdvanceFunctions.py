#Recursive (an function calling its own func)

def Fact(num:int):
    if num == 1:
        return num;
    else:
        output = num * Fact(num-1);
        return output;


ip = int(input("Please enter the number to find its factorial :"));

print("Factorial of - {} is {}:".format(ip,Fact(ip)));


#Anonymous function (lambda arguments : expression)

val = lambda x,y : x+y;

print(val(2,5));

#Majorly we use lambda functions inside a function

def fun(n):
    return lambda x : x ** n;

val = fun(2);

print(val(2)); # 2 ** 2
print(val(3)); # 3 ** 2    


# filter function filter(function,sequence) - picks only the true values

ages = [4,5,73,23,12,9]

def myFunction(x):
    if x < 12:
        return False
    else:
        return True

adults = filter(myFunction,ages)
print(f"Adults : { list(adults)}" )

# map function map(function,sequence) 

def calculatedata(x):
    return x * 2
ip = [5,6,8,9]

op = map(calculatedata,ip)

print(f" map output :  { list(op) }")


# reduce function

# generator function (return , yield)