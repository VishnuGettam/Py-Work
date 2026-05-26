"""
         father     
         |    | 
    child_1   child_2
"""


class Father():
    def Output_F(self):
        print("this is father class")

class Child_1(Father):
    def Output_C1(self):
        print("this is child_1 class")

class Child_2(Father):
    def Output_C2(self):
        print("this is from child_2 class")



print("-------Child_1-----------")
c1 = Child_1()
c1.Output_F()
c1.Output_C1()

print("-------Child_2-----------")
c2= Child_2()
c2.Output_F()
c2.Output_C2()