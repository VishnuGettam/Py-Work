"""
    Class Object creation  
        ||
    constructers (initialize the defaults) and can have only a single constructor
"""



class Person:
    
    # default constructor    
    def __int__(self):
        pass
    
    # parametirized constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def GetValue(self):
        print(f" User Name : {self.name}  && Age : {self.age} ")


p1 = Person(name="Mike",age=20)
p1.GetValue()


"""
    Alternative way to have multiple constructors is 
    1.default values to constructor method variables 
    2.*args / **keyargs
    3.classmethod
"""

class UserDetails():

    def __init__(self,name) -> None:
        self.name = name


    @classmethod
    def userdetails_constructor(cls,name,location):
        # imp here (need to initialize the default constructor) 
        # and add new params
        instance = cls(name)
        instance.location = location 

        return instance
    
    def Display_UserDetails(self):
        # getattr () acts a null safe access
        print(f"User Name : {self.name} && Location : { getattr(self,"location","N/A")   }")
    
user = UserDetails.userdetails_constructor("Ravi", "Bengaluru")
print(user.name)      # Ravi
print(user.location)  # Bengaluru

user.Display_UserDetails()

another_user = UserDetails(name="Mike")
print(another_user.name)

# below invocation will fail 
# print(another_user.location)

another_user.Display_UserDetails()