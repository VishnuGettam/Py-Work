#list concatenation

a = [1,3,15];
b = ["Alice",25,True];        

c = a + b;

print("Concatenated List : {}".format(c));  

#Append ( addd to the end of the list)
numbers = [10,20,30]; 

numbers.append(40);

print("List after append : {}".format(numbers));


#Insert(add at specific index)

numbers.insert(1,15); #.insert(index,value)

print("List after insert : {}".format(numbers));


#Remove (first instance of the matching object)

numbers.remove(15);  #.remove(value)

print("List after remove : {}".format(numbers));


#unknown remove

if 30 in numbers:
    numbers.remove(30);
    print("List after removing 30 : {}".format(numbers));


#Clear

numbers.clear(); #.clear()

print("List after clear : {}".format(numbers));

#pop (remove from the end of the list)

numbers = [10,20,30,40,50];

numbers.pop(); #.pop()

print("List after pop : {}".format(numbers));

#copy

numbers_copy = numbers.copy(); #.copy() - creates a copy of the list

print("List after copy : {}".format(numbers_copy));

#Delete 

del numbers_copy; # deletes the list


print(f" Append vs Extend ")
_agelist = [2,3,4,5]

_appendlist =[6,7,8]

_extendlist = [9.10,11]


# allows indivisual values/other lists 
print(f" extended list  : {_agelist.extend(_extendlist)} ")

# allows only indivisual values 
print(f" appended list :  {_agelist.append(_appendlist[0])} ")



