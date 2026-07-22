from typing import Any
import time

class ExecutionTimeDecorator:

    ## Initialize the decorator with the original function
    def __init__(self,original_function):
        self.original_function = original_function

    # Allow decorator instances to be called like functions
    def __call__(self, *args: Any, **kwds: Any):
        start_time = time.perf_counter()
        result=self.original_function(*args,**kwds)
        execution_time = time.perf_counter() - start_time
        print(
        f"{self.original_function.__name__} "
        f"executed in {execution_time:.6f} seconds"
            )
        return result
         

