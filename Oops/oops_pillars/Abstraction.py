"""
    Abstraction :-  hide unnecessary details 

        abstract class
        abstract methods

    using modules & inheritance , we implement abstraction in python
"""

# python defaul module for abstract class

# abc - module 
# ABC - class

from abc import ABC as default_abstract_class,abstractmethod


class Vehicle(default_abstract_class):

    def __int__(self,name,make):
        self.name = "Creta"
        self.make = "Hyundai"
        

# define abstract method
    @abstractmethod
    def Start_Vehicle(self):
        print(f" Vehicle {self.name} of from {self.make} has started ")

# define instance method 
    def Vehicle_Information(self):
        print()


class Car(Vehicle):

    def __int__(self,name,make):
        self.name = name
        self.make = make
        

    def Start_Vehicle(self):
        print(f" From Car class :- Vehicle {self.name} of from {self.make} has started  ")
    
    def Car_Horn(self):
        print("Vehicle is Horned")



# execution entry point 
if __name__ == "__main__":
  
  
  # abstract class compile time error  
    """
     v = Vehicle()       

     v.name = "GH"
     v.make = 1990

     v.Start_Vehicle()

     """

    c = Car()

    c.name = "Brezza"
    c.make = "Maruti" 

    c.Start_Vehicle()

   



