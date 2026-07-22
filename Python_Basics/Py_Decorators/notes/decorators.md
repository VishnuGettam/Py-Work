Enhance behavior (logging): A decorator can log when a function starts or ends.
Example: A @log_calls decorator prints “Calling function” before execution and “Function complete” after.

Modify inputs: A decorator can check or adjust inputs (e.g., ensure positive values).
Example: A @non_negative decorator ensures all arguments are non-negative and raises an error otherwise.

Modify outputs: A decorator can transform what’s returned (e.g., round results).
Example: A @round_result decorator rounds any returned number to two decimal places.

Access control: A decorator can restrict access based on conditions.
Example: An @admin_only decorator checks if the user is an admin before allowing the function to run.

Add state (e.g., count calls): A decorator can add attributes to the function (like counting how often it's called).
Example: A @count_calls decorator increments a function’s .call_count attribute each time it’s called.

Register functions: A decorator can add the function to a registry (like a plugin system).
Example: A @register_plugin decorator adds the function to a global plugins list.

The major use cases of decorators in Python are to encapsulate cross-cutting concerns. Specifically, they’re used to add logging, enforce access control, validate inputs, transform outputs, implement caching, track state (like function calls), or facilitate patterns like registering plugins. In essence, they streamline repetitive tasks that apply to multiple functions, ensuring clean, reusable code.