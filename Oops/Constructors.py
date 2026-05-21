"""
    Class Object creation  
        ||
    constructers (initialize the defaults)
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
    
    