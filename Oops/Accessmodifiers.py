
"""
Access modifiers -> Public,Private,Protected 
# but these are not enforsed

Public - pythons default - No restrictions
Private - only inside a class 
Protected - inside a class,derived class

"""


class Person:      

    def __init__(self,name,age):
        # protected variable (_)
        self._name = name
        self.age = age
        # private variable(__)
        self.__location = "Bangalore"


    def GetValue(self):
        print(f" User Name : {self._name} && Age : {self.age}  && location - {self.__location}")


if __name__ == "__main__":

    p1 = Person(name="Vishnu",age=30)
    p1.GetValue()

    print(f" Age : {p1.age}")
    
    # direct access to protected variable outside the class
    print(f" Name : {p1._name}")

    # error is thrown
    # print(f" Location : {p1._location} ")

    # can be accessed by _Classname__privatevariable
    print(f" Location : {p1._Person__location} ")
    



