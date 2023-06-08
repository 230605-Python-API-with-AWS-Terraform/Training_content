# Python Functions

Functions in Python are blocks of reusable code that perform specific tasks. They are a fundamental part of the Python programming language and are used to organize and modularize code. 

Here are some key aspects and features of Python functions:

**How to define a function**:

A function is defined using the def keyword, followed by the function name, parentheses (), and a colon :. The function body is indented below the definition.

```python

def greet():
    print("Hello, world!")

```
**Function Invocation**:

To execute a function, you simply invoke it by using its name followed by parentheses `()`.

```python

greet()  # Output: Hello, world!

```

**Function Parameters**:

Functions can accept input parameters, allowing you to pass values or arguments to the function for processing. Parameters are defined inside the parentheses of the function definition.

```python

def greet(name):
    print("Hello, " + name + "!")

greet("Revature")  # Output: Hello, Alice!

```

**How to return values**:

Functions can return values using the return statement. The returned value can be assigned to a variable or used directly in the code.

```python

def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)  # Output: 8

```

**How to provide default Parameters**:

You can provide default values for function parameters. If a value is not passed when invoking the function, the default value is used.

```python

def multiply(a, b=2):
    return a * b

print(multiply(3, 4))  # Output: 12
print(multiply(5))     # Output: 10 (default value of b is used)

```

**Variable Number of Arguments**:

Functions can accept a variable number of arguments using the `*args` or `**kwargs` syntax.

```python

def print_items(*args):
    for item in args:
        print(item)

print_items("apple", "banana", "cherry")  # Output: apple banana cherry

def print_dict(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + value)

print_dict(name="Alice", age="25")  # Output: name: Alice  age: 25

```

**Scope of Variables**:

Variables defined inside a function have local scope, meaning they can only be accessed within the function. Variables defined outside the function have global scope and can be accessed from anywhere in the code.

**Lambda Functions**:

Python also supports lambda functions, which are anonymous functions defined using the lambda keyword. They are typically used for small and one-time operations.

```python

double = lambda x: x * 2
print(double(5))  # Output: 10

```
**Nested Functions**

Python allows you to define functions within other functions. These nested functions are also known as inner functions. Inner functions can access variables from the enclosing function, providing a way to create more modular and specialized code.

```python

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

result = outer_function(5)
print(result(3))  # Output: 8
```

In this code snippet, we have two nested functions: `outer_function` and `inner_function`.

- The outer_function takes a parameter x.
- Inside the outer_function, we define the inner_function that takes a parameter y.
- The inner_function returns the sum of x and y.

The important thing to note here is that the inner_function has access to the variables defined in the `outer_function`. In this case, `inner_function` has access to the x variable.

- We invoke the outer_function with the argument 5 and assign the returned value to the variable result.
- The result now holds a reference to the inner_function with x set to 5.
- Finally, we call result(3), which executes the inner_function with y set to 3. This results in the sum of x (which is 5) and y (which is 3), giving us the output of 8.

