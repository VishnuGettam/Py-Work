"""
    father    mother
         |    | 
          child
"""


class Father():
    def Output_F(self):
        print("this is father class")

class Mother():
    def Output_M(self):
        print("this is mother class")

class Child(Father,Mother):
    def Output_C(self):
        print("this is from child class")


c1 = Child();
c1.Output_F()
c1.Output_M()
c1.Output_C()