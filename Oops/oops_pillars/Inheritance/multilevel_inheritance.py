"""
    GrandFather
        |
      Father
        |
    GrandChild
"""

class GrandFather():
    def Output_GF(self):
        print("this is from grandfather class")

class Father(GrandFather):
    def Output_F(self):
        print("this is from father class")

class Child(Father):
    def Output_C(self):
        print("this is from child class")


c1 = Child()
c1.Output_GF()
c1.Output_F()
c1.Output_C()