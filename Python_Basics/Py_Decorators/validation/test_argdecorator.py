from Py_Decorators.decorators.arg_decorator import NonNegative_Decorator as nc



@nc
def validate_numbers(*args):
    result = 0
    for x in args:
        result +=x
    return result

if __name__ == "__main__":
    op=validate_numbers(3,4,-5,6,7,8)
    print(f"{op}")
    print(validate_numbers.__name__)
    print(validate_numbers.__doc__)
    print(validate_numbers.__annotations__)

