#For Bitwise operations, it will convert the numbers into binary format and then perform the operations.

a = 10; 
b = 12;

print("Bitwise Operators in Python");

ans = a | b; # Bitwise OR

print ("a|b : ",ans);

ans = a & b; # Bitwise AND      

print ("a&b : ",ans);

ans = a ^ b; # Bitwise XOR

print ("a^b : ",ans); 

var = 4; # Bitwise Left Shift Operation

print ("var << 1 : ",var<<1);  # number * 2^n
print ("var << 2 : ",var<<2);  # number * 2^n
print ("var << 3 : ",var<<3);  # number * 2^n

var = 14; # Bitwise Right Shift Operation

print("var >> 1 : ",var>>1);  # number / 2^n
print("var >> 2 : ",var>>2);  # number / 2^n
print("var >> 3 : ",var>>3);  # number / 2^n  

var = 4 ; # Bitwise one's complement operation

print("var ~ : ", ~var); # -N = -(N+1)
     
