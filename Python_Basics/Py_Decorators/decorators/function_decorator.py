import time 


def Decorator_Function(func_name):
    def Wrapper_Function(*args,**kwargs):
        start_time = time.time()
        result = func_name(*args,**kwargs)
        execution_time = start_time - time.time()
        print(f"Function - {func_name.__name__} completed its execution in - {float(execution_time)} sec")
        return result
    return Wrapper_Function



@Decorator_Function
def sum_range():
    result = 0
    for x in range(1,100):
        result+=x
    return result


@Decorator_Function
def multiplication(a,b):
    result = a * b
    return result


if __name__ == "__main__":
    op=sum_range()
    print(f"sum range - {op} \n")

    mul = multiplication(45,20)
    print(f"Multiplication - {mul}")

    