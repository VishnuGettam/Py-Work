#Dictionary using Loop - Key/Value Pair Management

user_info = {
    "Name": "Alice",    
    "Age": 30,
    "Location" : "Bng"
};


# Looping through keys
print("Looping through keys:");
for key in user_info:
    print("Key: {}, Value: {}".format(key, user_info[key]));

#Dictionary items() method to loop through key-value pairs
print("\nLooping through key-value pairs using items():");

print(user_info.keys()); #prints all the keys in the dictionary
print(user_info.values()); #prints all the values in the dictionary

# Looping through key-value pairs
for key, value in user_info.items():
    print("Key: {}, Value: {}".format(key, value));


#Change values

user_info["Age"] = 31; #Updating Age

print("\nUpdated user_info:");

for key,value in user_info.items():
    print("Key: {}, Value: {}".format(key, value));
    
# Delete a key-value pair (pop)

removed_value = user_info.pop("Location"); #Removing Location

print("\nAfter removing 'Location' (value was: {}):".format(removed_value));

for key,value in user_info.items():
    print("Key: {}, Value: {}".format(key, value));

# Delete a key-value pair (del)

del user_info["Profession"]; #Removing Profession


# Clear entire dictionary
user_info.clear(); #Clearing all entries

# Delete the dictionary entirely
del user_info; #Deleting the dictionary

