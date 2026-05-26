numbers = [25,10,45,19,65,74];

#Slicing the list

#1
numbers_sl1 = numbers[0:3];
print("Sliced List from index 0 to 2 : {}".format(numbers_sl1));

#2
numbers_sl2 = numbers[:4];
print("Sliced List from start to index 3 : {}".format(numbers_sl2));

#3
numbers_sl3 = numbers[2:];
print("Sliced List from index 2 to end : {}".format(numbers_sl3));


#Reverse 
numbers_sl4 = numbers[::-1];

print("Reversed List : {}".format(numbers_sl4));

#Step Slicing
numbers_sl5 = numbers[0:6:2];

print("Sliced List with step 2 : {}".format(numbers_sl5));

#Reversed Slicing
numbers_sl6 = numbers[-6:-1];

print("Sliced List from negative index -6 to -2 : {}".format(numbers_sl6));

numbers_sl7 = numbers[-1:-6:-1];

print("Sliced List from negative index -1 to -6 : {}".format(numbers_sl7));

numbers_s18 = numbers[-6:];

print("Sliced List from negative index -6 to end : {}".format(numbers_s18));


#update the List
user_info = ["Bob",30,"Doctor","USA",False];

user_info[1:3] = [31,"Surgeon"];    

print("Updated List : {}".format(user_info));

#delete the List
del user_info[1:3];

print("List after deletion : {}".format(user_info));

user_info[1:3] = [] ;

print("List after emptying the list : {}".format(user_info));

user_info.clear();

print("List after clearing all elements : {}".format(user_info));
