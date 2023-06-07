## Python Datatypes

In Python, data types define the nature of the values you can store and manipulate in your programs. Here are some commonly used data types in Python:

**Numeric Types**:

`int`: Represents integer values (e.g., 42, -10, 0).

`float`: Represents floating-point or decimal values with fractional parts (e.g., 3.14, -0.5).

`complex`: Represents complex numbers in the form a + bj, where a is the real part, b is the imaginary part, and j represents the square root of -1.

```python
# Numeric types
age = 25
pi = 3.14
z = 2 + 3j

print(age)  # Output: 25
print(pi)   # Output: 3.14
print(z)    # Output: (2+3j)

```

**Sequence Types**:

- `str`: Represents a sequence of characters or text (e.g., "Hello, World!").

- `list`: Represents an ordered collection of items, which can be of different types (e.g., [1, 2, 3]).

- `tuple`: Similar to a list, but it is immutable (i.e., its values cannot be modified once defined) (e.g., (1, 2, 3)).

-`range`:

**Mapping Type**:

- `dict`: Represents a collection of key-value pairs, where each key is unique (e.g., {'name': 'John', 'age': 25}).

**Set Types**:

- `set`: Represents an unordered collection of unique elements (e.g., {1, 2, 3}).

**Boolean Type**:

- `bool`: Represents a Boolean value (True or False), used for logical operations and control flow.

**None Type**:

- `None`: Represents the absence of a value or a null value.

```python

# Numeric types
age = 25
pi = 3.14

# String type
name = "John Doe"

# List type
numbers = [1, 2, 3]

# Tuple type
coordinates = (10, 20)

# Dictionary type
person = {'name': 'John', 'age': 25}

# Set type
unique_numbers = {1, 2, 3}

# Boolean type
is_valid = True

# None type
result = None

```

These data types provide different functionalities and operations in Python. Additionally, Python allows you to convert values between different data types using built-in functions like `int(), float(), str(), list(), tuple(), dict(), set(),` etc.

---

## Python casting

In Python, casting refers to the process of converting a value from one data type to another. Python provides several built-in functions that allow you to perform casting. 

Here are the commonly used casting functions:

- `int()`: Converts a value to an integer. If the value is a float, it truncates the decimal part. If the value is a string, it converts a valid integer string to an integer.
```python
num_float = 3.14
num_int = int(num_float)
print(num_int)  # Output: 3

num_string = "42"
num_int = int(num_string)
print(num_int)  # Output: 42
```

- `float()`: Converts a value to a floating-point number. It can convert an integer, a string representation of a number, or another float.
```python
num_int = 42
num_float = float(num_int)
print(num_float)  # Output: 42.0

num_string = "3.14"
num_float = float(num_string)
print(num_float)  # Output: 3.14
```

- `str()`: Converts a value to a string. It can convert an integer, a float, a boolean, or any other object to its string representation.
```python
num_int = 42
num_string = str(num_int)
print(num_string)  # Output: "42"

num_float = 3.14
num_string = str(num_float)
print(num_string)  # Output: "3.14"

is_valid = True
bool_string = str(is_valid)
print(bool_string)  # Output: "True"
```

- `list()`: Converts a sequence (like a string or tuple) to a list.
```python
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3]

my_string = "Hello"
my_list = list(my_string)
print(my_list)  # Output: ['H', 'e', 'l', 'l', 'o']
```

- `tuple()`: Converts a sequence (like a list or string) to a tuple.
```python

my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)

my_string = "Hello"
my_tuple = tuple(my_string)
print(my_tuple)  # Output: ('H', 'e', 'l', 'l', 'o')
```

These are just a few examples of casting functions in Python. The appropriate casting function depends on the source and target data types you want to convert between. By using these functions, you can convert values between different data types as needed in your programs.

---

## Python Operators

In Python, operators are symbols or special characters that perform various operations on operands (variables or values). Here are the different types of operators available in Python:

**Arithmetic Operators**:

- `+ (addition)`: Adds two operands.
- `- (subtraction`): Subtracts the second operand from the first.
- `* (multiplication)`: Multiplies two operands.
- `/ (division)`: Divides the first operand by the second, returning a float.
- `% (modulo)`: Returns the remainder after division.
- `// (floor division)`: Divides the first operand by the second and returns the largest whole number less than or equal to the result.
- `** (exponentiation)`: Raises the first operand to the power of the second.

**Assignment Operators**:

- `= (assignment)`: Assigns the value on the right to the variable on the left.
- `+= (add and assign)`: Adds the value on the right to the variable on the left and assigns the result to the variable on the left.
- `-= (subtract and assign)`: Subtracts the value on the right from the variable on the left and assigns the result to the variable on the left.
- `*= (multiply and assign)`: Multiplies the variable on the left by the value on the right and assigns the result to the variable on the left.
- `/= (divide and assign)`: Divides the variable on the left by the value on the right and assigns the result to the variable on the left.
- `%= (modulo and assign)`: Performs modulo division on the variable on the left by the value on the right and assigns the remainder to the variable on the left.
- `//= (floor divide and assign)`: Performs floor division on the variable on the left by the value on the right and assigns the result to the variable on the left.
- `**= (exponentiate and assign)`: Raises the variable on the left to the power of the value on the right and assigns the result to the variable on the left.

**Comparison Operators**:

- `== (equal to)`: Checks if the operands are equal.
- `!= (not equal to)`: Checks if the operands are not equal.
- `< (less than)`: Checks if the left operand is less than the right.
- `> (greater than)`: Checks if the left operand is greater than the right.
- `<= (less than or equal to)`: Checks if the left operand is less than or equal to the right.
- `>= (greater than or equal to)`: Checks if the left operand is greater than or equal to the right.

**Logical Operators**:

- `and`: Returns True if both operands are True.
- `or`: Returns True if at least one of the operands is True.
- `not`: Returns the opposite boolean value of the operand.

**Bitwise Operators**:

- `& (bitwise AND)`: Performs a bitwise AND operation between the operands.
- `| (bitwise OR)`: Performs a bitwise OR operation between the operands.
- `^ (bitwise XOR)`: Performs a bitwise XOR (exclusive OR) operation between the operands.
- `~ (bitwise NOT)`: Performs a bitwise NOT operation on the operand, inverting each bit.
- `<< (left shift)`: Shifts the bits of the left operand to the left by the number of positions specified by the right operand.
- `>> (right shift)`: Shifts the bits of the left operand to the right by the number of positions.

**Sample code**

```python

# Arithmetic Operators
a = 10
b = 3

print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333333333333335
print(a % b)  # Output: 1
print(a // b) # Output: 3
print(a ** b) # Output: 1000

# Assignment Operators
x = 5
x += 2
print(x)  # Output: 7

y = 10
y -= 3
print(y)  # Output: 7

# Comparison Operators
p = 7
q = 5

print(p == q)  # Output: False
print(p != q)  # Output: True
print(p < q)   # Output: False
print(p > q)   # Output: True
print(p <= q)  # Output: False
print(p >= q)  # Output: True

# Logical Operators
is_true = True
is_false = False

print(is_true and is_false)  # Output: False
print(is_true or is_false)   # Output: True
print(not is_false)          # Output: True

# Bitwise Operators
m = 10  # Binary: 1010
n = 6   # Binary: 0110

print(m & n)   # Output: 2 (Binary: 0010)
print(m | n)   # Output: 14 (Binary: 1110)
print(m ^ n)   # Output: 12 (Binary: 1100)
print(~m)      # Output: -11 (Binary: -1011)
print(m << 2)  # Output: 40 (Binary: 101000)
print(m >> 2)  # Output: 2 (Binary: 10)

```
---