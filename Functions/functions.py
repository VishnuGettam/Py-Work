#Simple function

#Default arguements (year)
def display(day,month,year:int = 2019):
    print("Day - {}".format(int(day)));
    print("Month - {}".format(int(month)));
    print("Year - {}".format(int(year)));


display(4,5);
    
#Keyword arguments (we can assign the arguments in any pattern)
def UserInformation(name,place,age):
    print("Name - {} && Place - {} && Age - {} .".format(name,place,age));


UserInformation(age=30,name="Alice",place="Bng");    


#Arbitraty arguments (If we dont know on how many arguments to pass)
def sum(*args):
    ans=0;
    for x in args:
       ans = ans + x;
    return ans; 
    
print("Sum of 10 & 20 - {}".format(sum(10,20)));
print("Sum of 10 & 20 & 30 - {}".format(sum(10,20,30)));
print("Sum of 10 & 20 & 30 & 40 - {}".format(sum(10,20,30,40)));


#function with return statement

def fun():
    return 10 , 20;

a,b = fun();

print(a);
print(b); 