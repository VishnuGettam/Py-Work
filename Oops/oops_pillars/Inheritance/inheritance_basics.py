"""
Inheritance - Code reusability 
    Single 
    Multiple  -> Father,Mother : child
    Multilevel -> x (Grand parent) -> y (parent) -> z (child)
    Hierarchial 
    Hybrid
"""

# Single Inheritance


class Person:

    age = 30
    
    def __init__(self,name):
        self.name = name


    def UserName(self):
        print(f" UserName is : {self.name} && age is : {self.age} ")


class Student(Person):

    def __int__(self,name,school_name):
        super().__init__(name)
        self.school_name = school_name


    def StudentDetails(self):
        print(f" UserName - {self.name} && age : {self.age} && school : {self.school_name}")


if __name__ == "__main__":
    p1 = Person("vihaan")

    p1.UserName()


    s1 = Student("vishnu")
    s1.school_name = "CRR"

    s1.StudentDetails()