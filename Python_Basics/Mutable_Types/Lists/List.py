
#lists 
numbers = [10, 20, 30, 40, 50];

#display numbers list
print(numbers);

#Iterate through the list and print each number
for x in numbers:
    print(x);
    
#Check if a number exists in the list

#Method 1
for x in numbers:
    if x == 30:
        print("30 is found in the list");
#Method 2
if 20 in numbers:
    print("20 is found in the list");


#Heterogeneous list
userDetails = ["Alice",25,"Engineer","India",True];

print(userDetails);


