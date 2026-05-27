"""
    Single Inheritance : Parent -> child
"""

# Parent Class
class Vehicle():

    # constructor
    def __init__(self,name,make,year):
        self.name = name
        self.make = make
        self.year = year


    def Vehicle_Details(self):
        print(f" Vehicle is {self.name} from {self.make} release in {self.year}  ")


# Child Class
class Brezza(Vehicle):
    def __int__(self):
        pass

# calling base method 
    def Vehicle_Details(self):
        super().Vehicle_Details()
        # print(f" Vehicle is {self.name} from {self.make} , released in {self.year} .")
 





# Entry point execution
if __name__ == "__main__":
    brezza_obj = Brezza(name="Brezza",make="Maruti",year="2025")
    brezza_obj.Vehicle_Details()