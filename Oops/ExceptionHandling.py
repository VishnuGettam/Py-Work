"""
    Handling the exception in run time 
        try:
        exception:
        finally:
"""


class Person:
    def __int__(self):
        pass

    def UserInformation(self,info):

        try:
            for val in info:
                print(val)

        except Exception as e:
            print( f" Exception Details : {e}")

        finally:
            print("Finally block \n UserInformation completed its execution")



if __name__ == "__main__":
    userDetails = ["Vihaan","Gettam","Blr"]

    p1 = Person()

    p1.UserInformation(userDetails)