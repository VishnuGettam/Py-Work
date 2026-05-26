str = "Python Programming"

print("Original String: ", str);

for x in str:
    print(x);
    
#Check for the character 'P' in the string
for y in str:
    if y == "P":
        print("Character 'P' found in the string");
        break;