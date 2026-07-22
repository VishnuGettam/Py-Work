"""
            Single entity  - multiple forms 
                Method overloading : same class
                Method overriding : inheritance
"""


print("----------Method Overloading------------")

# Method Overloading 
class UserInformation:
    def __int__(self):
        pass


    def UserDetails(self,name=None,age=None,location=None):
        print(f"user with name : {name} && age && {age} && location {location}")



userinfo_obj = UserInformation()

userinfo_obj.UserDetails()
userinfo_obj.UserDetails("Mike")
userinfo_obj.UserDetails("Kerry",30)
userinfo_obj.UserDetails("John",32,"blr")

print("----------Method Overriding------------")

# Method Overriding


class Father():
    def Output(self):
        print("this is from father class")

class Child(Father):
    def Output(self,name=None):
        print(f"this is from child class with of {name}")
        # parent class function execution
        super().Output()



child_obj = Child()
child_obj.Output("Jk")