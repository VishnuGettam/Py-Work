"""
    Types of attributes 
        Object  -> object specific 
        Class   -> same for all objects
"""



class Person:
    # class parameters
    city = "Bangalore"
    
    
    def __init__(self,name,age):
    # instance or object parameters
        self.name = name
        self.age = age
        
    def GetValue(self):
        # call class params with "self"
        print(f"  Use Name : {self.name}  && Age : {self.age}  && city : {self.city} ")
        
        #call class params with Person (class name)
        print(f"  Use Name : {self.name}  && Age : {self.age}  && city : {Person.city} ")
        
        

if __name__ == "__main__":
    p1 = Person('Vishnu',20)
    
    p1.GetValue()
    