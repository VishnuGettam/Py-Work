"""
    GrandFather
        |
      Father
        |
    GrandChild
"""

class GrandFather():
    # protected
    _y = 10
    # private
    __x = 20 

    def Output_GF(self):
        print(f"this is from grandfather class && variables : _y -> {self._y} && _x -> {self.__x}")

class Father(GrandFather): 

    def Output_F(self):
        print(f"this is from father class && variables : _y -> {super()._y} && _x ->")
              # {super().__x}")

class Child(Father): 

    def Output_C(self):
        print(f"this is from child class && variables : _y -> {super()._y} && _x -> ")
              # {super().__x}")


c1 = Child()
c1.Output_GF()
c1.Output_F()
c1.Output_C()