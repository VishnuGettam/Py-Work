"""
control statements : 
    if/else/nestedifelse
"""


def User_Age(age:int):

    if age is None:
        print("Age shouldn't be a 'null' or 'empty' ")
    elif(age <10):
        print("Kids")
    elif(age > 10 and age < 18):
        print("Age is between 10 - 18")
    else:
        print("Age is adult")


if __name__ == "__main__":
    _age = int(input("Please enter user age : "))
    User_Age(_age)
