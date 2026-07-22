
# argurments decorator with functionality to validate the negative values

def NonNegative_Decorator(func):
    def Wrapper_Function(*args,**kwargs):
        # validate the arguements
        result = True
        if len(args) > 0 :
            for x in args:
                if(x) < 0:
                    result = False
                    break

        if(result == False):
            return "Holds Negative Number"
        else:
            return func(*args,**kwargs)        

    return Wrapper_Function          



