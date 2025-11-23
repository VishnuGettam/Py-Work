#Length of Tuples

user_names = ("Alice", "Bob", "Charlie", "Diana");

print("Length of user_names tuple : {}".format(len(user_names)));

#Display the tuple
for name in user_names:
    print(name);

#Check if an element exists in the tuple
if "Bob" in user_names:
    print("Bob is found in the tuple");
    
#Concatenation of Tuples
tuple1 = (1, 2, 3);
tuple2 = (4, 5, 6);

tuple3 = tuple1 + tuple2;

print("Concatenated Tuple : {}".format(tuple3));


#Counting elements in a Tuple
tuple4 = (1, 2, 2, 3, 4, 2, 5);
count_2 = tuple4.count(2);
print("Number of times 2 appears in tuple4 : {}".format(count_2));


#Finding index of an element in a Tuple
tuple5 = ("apple", "banana", "cherry", "date");
cherry_index = tuple5.index("cherry");

print("Index of 'cherry' in tuple5 : {}".format(cherry_index));