from Py_Decorators.decorators.execution_time import ExecutionTimeDecorator  as ec


@ec
def sum(a,b,c,d):
    return a + b + c + d;


if __name__ == "__main__":
    op = sum(5,677,8,3)
    print(f"Sum - {op}")