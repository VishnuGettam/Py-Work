#Dictionary - Key/Value Pair Management

data = {  "Key":"Value","Key":"Value" };

user_info = {
    "Name": "Alice",
    "Age": 30,
    "Location" : "Bng"
};

print(user_info);

# Accessing value by key
print(user_info["Name"]);

# Adding a new key-value pair
user_info["Profession"] = "Engineer";

print(user_info);

#check if key exists
age_key = "Age" ;

if age_key in user_info:
    print("Key 'Age' is available and its value : {}".format(user_info[age_key]));
else:
    print("Key not found");

# Removing a key-value pair
del user_info["Location"];