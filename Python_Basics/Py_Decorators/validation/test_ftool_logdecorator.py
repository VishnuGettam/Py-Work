from Py_Decorators.decorators.ftool_logdecorator import Log_Decorator as ld



@ld
def sum(a:int,b:int):
    """ sum the numbers  """
    return a+b


if __name__ == "__main__":
    op = sum(4,7)
    print(f"sum ouput - {op}")

    # using functiontool.wrap , the function - (sum) will holds its metadata information eventhough it is wrapped in decorator
    print(f" Function Name - {sum.__name__}")
    print(f" Function Docs - {sum.__doc__}")
    print(f" Function Annotations - {sum.__annotations__}")
    help(sum)