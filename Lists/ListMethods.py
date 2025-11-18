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


#Remove

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



