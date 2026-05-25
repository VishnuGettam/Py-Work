def UserInformation(*args):

    for x in args:
        print(x)


UserInformation(4,5,6,7,"vishnu")

print("---------Keyword arguements----------")

def KeyInformation(**args):
    for x in args:
        print(args[x])


KeyInformation(name="vishnu",location="blr",sal=231)