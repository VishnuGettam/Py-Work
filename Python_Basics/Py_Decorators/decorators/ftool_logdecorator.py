import functools

# decorator log the function execution details
def Log_Decorator(func):
    @functools.wraps(func)  # <-- preserves func's identity
    def wrapper(*args,**kwargs):
        
        print(f" Function  - {func.__name__} started execution")
        result = func(*args,**kwargs)
        print(f" Function  - {func.__name__} completed execution")
        return result
    return wrapper


