# OOPS - Object Oriented Programming System

# Inheritance
# Polymorphism
# Abstraction 
# Encapsulation

# The class `Person` defines methods to set and get a person's name and age, and allows user input to
# set these values and display them.


class Person:
    
    def SetValue(self,name,age):
        self.name = name
        self.age = age
    
    def GetValue(self):
        # formatted string literal 
        print(f"Name : {self.name} && Age : {self.age}") 
        

if __name__ == "__main__":
    
    # p1 object creation
    p1 = Person()
    
    # self is object reference (p1 reference)
    
    ip_name = input("Enter Name : ")
    ip_age = int(input("Enter Age : "))
    
    p1.SetValue(ip_name,int(ip_age))
    p1.GetValue()
    
    # p2 object creation
    p2 = Person()
    
    p2.name = "Vishnu"
    p2.age = 28
    
    p2.GetValue()