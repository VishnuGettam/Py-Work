a,b = 5, 10

#Logical OR Operator (||)
res = (a > 0) or (b < 5)
print("Logical OR Operator: ", res);

#Logical AND Operator (&&)
res = (a > 0) and (b < 15)
print("Logical AND Operator: ", res);

#Logical NOT Operator (!)
res = not(a > b)
print("Logical NOT Operator: ", res);

#Logical XOR Operator (^)
res = (a > 0) ^ (b < 5)
print("Logical XOR Operator: ", res);

#Logical NAND Operator
res = not((a > 0) and (b < 15))
print("Logical NAND Operator: ", res);

#Logical NOR Operator
res = not((a > 0) or (b < 5))
print("Logical NOR Operator: ", res);

#Logical XNOR Operator
res = not((a > 0) ^ (b < 5))
print("Logical XNOR Operator: ", res);



