user_information = {
    "Name": "Alice",
    "Age": 30,
    "Location": "Bng",
    "Profession": "Engineer"
};

# dictionary copy

new_info = user_information.copy();

print("New Info Copied from User Information:");
for key,value in new_info.items():
    print("Key: {}, Value: {}".format(key, value));
    
#dict method

user_details = dict(user_information);

print("\nUser Details created using dict() method:");
for key,value in user_details.items():
    print("Key: {}, Value: {}".format(key, value));