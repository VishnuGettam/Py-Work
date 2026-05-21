"""
Methods : 
     Static method   -> only "self" as input params
     Instance method -> can have its own params
"""

# The class `Person` defines an instance method `GetValue` to display the name and age of a person,
# and a static method `GetValue_StaticMethod` for static method execution.

class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
            
    def GetValue(self):
        print(f" Display from Instance Method : \n  UserName : {self.name} && Age : {self.age}  ")
    
    
    @staticmethod
    def GetValue_StaticMethod():
        print(f"Static Method execution")



if __name__ == "__main__":
    p1 = Person(name="Vihaan",age=8)
    
    # p1 Object
    p1.GetValue()    
    p1.GetValue_StaticMethod()
    
    #p2 Object
    p2 = Person("Vishnu",4)    
    p2.GetValue()    
    p2.GetValue_StaticMethod()