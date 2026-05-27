"""
    Errors  -> compiletime 
               runtime 

               
    Handling the runtime exception 
        try:
        exception:
        else:
        finally:
"""


class Person:
    def __int__(self):
        pass

    def UserInformation(self,info):

        try:
            for val in info:
                print(val)
        except ValueError as ve:
            print(f" Value error - {ve}")
        except Exception as e:
            print( f" Exception Details : {e}")
        else:
            print("No Exceptions on code execution ")
        finally:
            print("Finally block \n UserInformation completed its execution")



if __name__ == "__main__":
    userDetails = ["Vihaan","Gettam","Blr"]

    p1 = Person()
    p1.UserInformation(userDetails)