name = "Python";
year = 2025;

#using comma
print("Name : ",name,"Year : ",year);

#string concatination
print("Name : " + name + " Year : " + str(year));

#using format method    
print("Name : {} Year : {}".format(name,year));

#using format method with positional arguments
print("Name : {0} Year : {1}".format(name,year));

#using format method with keyword arguments
print("Name : {n} Year : {y}".format(n=name,y=year));

#using f-string (simple)
print(f"Name : {name} Year : {year}");

print(F"Name : {name} Year : {year}");